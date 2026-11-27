# Smart Traffic Signal Control Using Reinforcement Learning to Minimize Vehicle Waiting Time

## Project Overview

This project implements an intelligent traffic signal control system using **Reinforcement Learning (RL)** to minimize vehicle waiting time and improve traffic flow at an intersection.

The project compares a conventional fixed-timer traffic signal control system with an intelligent RL-based traffic control system.

The RL agent uses a trained Q-table to dynamically control traffic signals based on traffic conditions.

## Project Objectives

- Implement conventional fixed-timer traffic signal control.
- Develop an intelligent traffic signal control system using Reinforcement Learning.
- Dynamically manage traffic signals using a trained Q-table.
- Compare the performance of conventional and intelligent traffic control systems.
- Analyze cumulative vehicle waiting time and queue lengths.

## Technologies Used

- Python 3.x
- SUMO (Simulation of Urban Mobility)
- TraCI
- SUMOlib
- NumPy
- Matplotlib
- Reinforcement Learning

## Project Components

| Component | Description |
|---|---|
| Fixed Control Baseline | Conventional fixed-timer traffic signal control |
| RL Intelligent Control | Intelligent traffic signal control using a trained RL agent |
| Intersection Network | SUMO intersection network configuration |
| Simulation Configuration | Simulation configuration files |
| Traffic Flow | Traffic flow definition files |
| Trained Q-Table | Pre-trained Q-table used by the RL agent |
| Results and Analysis | Performance comparison graphs and learning curve |

## Project Workflow

### 1. Conventional Traffic Signal Control

The fixed-timer control system manages traffic signals using predefined timings.

**File:** `Fixed_Control_Baseline.py`

### 2. Intelligent Traffic Signal Control Using RL

The Reinforcement Learning agent uses the trained Q-table to control traffic signals dynamically according to traffic conditions.

**File:** `RL_Control_Intelligent.py`



## Results and Analysis

The project includes the following result visualizations:

**1. Comparison Bar Chart**

Comparison of the performance of the traffic control approaches.

**2. Learning Curve Graph**

Visualization of the learning progress of the Reinforcement Learning agent.

Both graphs are available in the `Results_and_Analysis` folder.

## Software Requirements

- Python 3.x
- SUMO Simulator
- Required Python libraries

## Installation and Setup

### Step 1: Install SUMO

Install the SUMO simulator and configure the `SUMO_HOME` environment variable.

### Step 2: Install Python Libraries

Run the following command:

```bash
pip install traci sumolib numpy matplotlib
```

### Step 3: Extract Project Files

Extract the required ZIP files into the project directory while preserving the original folder and file structure.

Ensure that the simulation configuration, intersection network, traffic flow files, and trained Q-table are available in their expected locations.

## How to Run the Project

### Step 1: Run the Conventional System (Baseline)

```bash
python Fixed_Control_Baseline.py
```

Observe the traffic build-up and cumulative waiting time displayed in the terminal.

### Step 2: Run the Intelligent System (RL Agent)

```bash
python RL_Control_Intelligent.py
```

The agent uses the trained Q-table (`Trained_QTable_Data.pkl`) to control traffic dynamically.



## Conclusion

This project demonstrates the application of Reinforcement Learning in intelligent traffic signal management. It compares conventional fixed-timer control with an RL-based intelligent approach and evaluates their performance through traffic waiting time and queue length analysis.

## Future Scope

- Extend the system to multiple intersections.
- Improve traffic signal optimization using advanced Reinforcement Learning algorithms.
- Explore real-time traffic data integration.
- Enhance traffic management for varying traffic conditions.

---

**Project Title:** Smart Traffic Signal Control Using Reinforcement Learning to Minimize Vehicle Waiting Time

**Developed by:** Rochana S
