# Distributed Task Scheduler Simulator

This repository contains a simulation of a distributed task scheduler for high-performance computing systems. The project demonstrates the design and implementation of a task scheduling algorithm tailored for a parallel supercomputer architecture. The system accounts for resource constraints, task dependencies, dynamic load balancing, and varying hardware characteristics.

---

## Features
- **Resource-Aware Scheduling**: Tasks are allocated based on available memory, computing power, and node capacity.
- **Dynamic Load Balancing**: Supports dynamic task reallocation when system conditions change (e.g., task completion, node failure).
- **Task Dependencies**: Handles dependencies to ensure tasks are executed in the correct order.
- **Customizable Topologies**: Simulates different hardware topologies with latency and bandwidth considerations.
- **Support for Heterogeneous Nodes**: Models hardware-specific capabilities such as GPU or FPGA acceleration.

---

## Requirements

To run the simulation, you need:
- Python 3.7 or higher
- Libraries: `random`, `time`, `queue`

Install additional dependencies (if any):
```bash
pip install -r requirements.txt
```

---

## Usage

### Step 1: Initialize Nodes
Define a set of computational nodes with specific resources (e.g., memory, computing power):
```python
nodes = [Node(node_id=i, total_memory=100, computing_power=50) for i in range(3)]
```

### Step 2: Create Tasks
Generate tasks with varying complexity, memory requirements, and priorities:
```python
tasks = [Task(task_id=i, complexity=random.randint(10, 100), memory_needed=random.randint(10, 30), priority=random.randint(1, 5)) for i in range(10)]
```

### Step 3: Schedule and Execute
Use the scheduler to assign tasks to nodes and process them:
```python
scheduler = Scheduler(nodes)
for task in tasks:
    scheduler.add_task(task)

scheduler.schedule_tasks()
scheduler.execute()
```

---

## Algorithm Overview
The scheduling algorithm operates in three main phases:
1. **Task Allocation**: Tasks are sorted by priority (lower value = higher priority) and allocated to the first available node with sufficient memory.
2. **Dynamic Reallocation**: If system conditions change (e.g., task completion or node failure), tasks are dynamically reassigned to maintain optimal utilization.
3. **Task Processing**: Each node processes its assigned tasks based on their complexity and its computing power.

Key considerations include minimizing idle time, balancing load across nodes, and adhering to task dependencies when scheduling.

---

## File Structure
- `scheduler.py`: Core implementation of the task scheduler.
- `node.py`: Node class representing computational units.
- `task.py`: Task class defining task attributes and priority logic.
- `main.py`: Entry point for running the simulation.
- `requirements.txt`: List of dependencies.

---

## Future Work
- Implement advanced scheduling algorithms (e.g., genetic algorithms or reinforcement learning).
- Integrate real-world hardware metrics for more realistic simulations.
- Expand support for multi-level task dependencies and workflows.

---

## License
This project is licensed under the MIT License. See `LICENSE` for details.

---

## Contributions
Contributions are welcome! Feel free to open issues or submit pull requests to improve the simulator.

---

## Contact
For questions or feedback, please open an issue in this repository.

