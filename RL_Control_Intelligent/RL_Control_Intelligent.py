import traci
import pickle
import os

# Configuration
ACTION_NAMES = {0: "GREEN: North-South", 2: "GREEN: East-West"}
LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.9
Q_TABLE_FILE = "q_table.pkl"

# Load the Brain
if os.path.exists(Q_TABLE_FILE):
    with open(Q_TABLE_FILE, "rb") as f:
        q_table = pickle.load(f)
else:
    q_table = {}

def get_density_level(n):
    if n == 0: return 0
    elif n <= 2: return 1
    elif n <= 5: return 2
    elif n <= 10: return 3
    return 4

traci.start(["sumo-gui", "-c", "simulation.sumocfg"])
EDGES = ["-E0", "-E1", "-E2", "-E3"]
step = 0
total_waiting_time_rl = 0
prev_state = None
prev_action = None

print(f"\n{'Step':<8} | {'Traffic State':<20} | {'Mode':<15} | {'Update'}")
print("-" * 70)

while step < 1000:
    traci.simulationStep()
    
    # 1. Calculate Reward (Negative Waiting Time)
    current_waiting = sum([traci.vehicle.getWaitingTime(v) for v in traci.vehicle.getIDList()])
    total_waiting_time_rl += current_waiting
    reward = -current_waiting 

    if step % 20 == 0:
        curr_s = tuple([get_density_level(traci.edge.getLastStepVehicleNumber(e)) for e in EDGES])
        
        # 2. UPDATE BRAIN (If we had a previous state)
        if prev_state is not None:
            if curr_s not in q_table:
                q_table[curr_s] = {0: 0.0, 2: 0.0}
            
            # Q-Learning Formula: Update the previous state based on the result
            best_future_q = max(q_table[curr_s].values())
            old_q = q_table[prev_state][prev_action]
            new_q = old_q + LEARNING_RATE * (reward + DISCOUNT_FACTOR * best_future_q - old_q)
            q_table[prev_state][prev_action] = new_q
            update_msg = "Value Updated"
        else:
            update_msg = "Starting..."

        # 3. DECIDE
        if curr_s in q_table and any(q_table[curr_s].values()):
            action = max(q_table[curr_s], key=q_table[curr_s].get)
            mode = "Q-TABLE"
        else:
            # Smart Adaptive Fallback for New States
            ns = curr_s[0] + curr_s[1]
            ew = curr_s[2] + curr_s[3]
            action = 0 if ns >= ew else 2
            mode = "NEW (ADAPTIVE)"
            if curr_s not in q_table:
                q_table[curr_s] = {0: 0.0, 2: 0.0}

        traci.trafficlight.setPhase("J0", action)
        print(f"{step:<8} | {str(curr_s):<20} | {mode:<15} | {update_msg}")
        
        prev_state = curr_s
        prev_action = action
        
    step += 1

traci.close()

# 4. SAVE THE IMPROVED BRAIN
with open(Q_TABLE_FILE, "wb") as f:
    pickle.dump(q_table, f)

print(f"\nFinal Waiting Time: {total_waiting_time_rl}")
print(f"Brain updated and saved! New total states: {len(q_table)}")