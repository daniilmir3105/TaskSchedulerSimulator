import random
import time
from queue import PriorityQueue

class Task:
    def __init__(self, task_id, complexity, memory_needed, priority, dependencies=None):
        self.task_id = task_id
        self.complexity = complexity
        self.memory_needed = memory_needed
        self.priority = priority  # lower value = higher priority
        self.dependencies = dependencies if dependencies else []
        self.is_completed = False
        
    def __lt__(self, other):
        return self.priority < other.priority
    
    def __repr__(self):
        return f"Task({self.task_id}, Priority={self.priority}, Complexity={self.complexity})"

class Node:
    def __init__(self, node_id, total_memory, computing_power, network_latency=0):
        self.node_id = node_id
        self.total_memory = total_memory
        self.used_memory = 0
        self.computing_power = computing_power
        self.network_latency = network_latency  # in seconds
        self.task_queue = []
        self.available = True
        
    def is_available(self, task):
        return self.used_memory + task.memory_needed <= self.total_memory
        
    def allocate_task(self, task):
        if self.is_available(task):
            self.used_memory += task.memory_needed
            self.task_queue.append(task)
            return True
        return False
    
    def release_task(self, task):
        if task in self.task_queue:
            self.used_memory -= task.memory_needed
            self.task_queue.remove(task)

    def process_tasks(self):
        if self.task_queue:
            task = self.task_queue.pop(0)
            # Simulate processing with time proportional to complexity and computing power
            time_to_process = task.complexity / self.computing_power + self.network_latency
            time.sleep(time_to_process)
            task.is_completed = True
            self.release_task(task)
            return task
        return None

class Scheduler:
    def __init__(self, nodes):
        self.nodes = nodes
        self.task_queue = PriorityQueue()
        
    def add_task(self, task):
        self.task_queue.put(task)
        
    def schedule_tasks(self):
        # Step 1: Scheduling tasks based on priority
        while not self.task_queue.empty():
            task = self.task_queue.get()
            scheduled = False
            # Step 2: Check dependencies
            if all(dep.is_completed for dep in task.dependencies):
                for node in self.nodes:
                    if node.allocate_task(task):
                        scheduled = True
                        print(f"Task {task.task_id} scheduled on Node {node.node_id}")
                        break
                if not scheduled:
                    print(f"Task {task.task_id} could not be scheduled (no available resources)")
            else:
                print(f"Task {task.task_id} waiting for dependencies")

    def execute(self):
        # Step 3: Execute tasks on nodes
        for node in self.nodes:
            completed_task = node.process_tasks()
            if completed_task:
                print(f"Task {completed_task.task_id} completed on Node {node.node_id}")
                # Dynamically reassign task if a node is not available
                if not node.is_available(completed_task):
                    self.reassign_task(completed_task)
                
    def reassign_task(self, task):
        # Try to reassign task to another node if the current node becomes unavailable
        for node in self.nodes:
            if node.allocate_task(task):
                print(f"Task {task.task_id} reassigned to Node {node.node_id}")
                return
        print(f"Task {task.task_id} could not be reassigned to any node")

# Example of use:
nodes = [Node(node_id=i, total_memory=100, computing_power=50, network_latency=random.uniform(0.1, 0.5)) for i in range(3)]
scheduler = Scheduler(nodes)

# Create tasks with dependencies and random priority
tasks = [
    Task(task_id=i, 
         complexity=random.randint(10, 100), 
         memory_needed=random.randint(10, 30), 
         priority=random.randint(1, 5), 
         dependencies=[random.choice([None, random.choice([i for i in range(i)])])]) 
    for i in range(10)
]

for task in tasks:
    scheduler.add_task(task)

scheduler.schedule_tasks()
scheduler.execute()
