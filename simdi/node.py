import threading
import time
import random
from config import NODE_CPU, NODE_MEMORY, NODE_STORAGE, ENABLE_FAULTS, FAULT_PROBABILITY
from storage import Storage

class Node:
    def __init__(self, node_id, network):
        self.node_id = node_id
        self.cpu = NODE_CPU
        self.memory = NODE_MEMORY  # GB
        self.storage = NODE_STORAGE  # GB
        self.available_memory = NODE_MEMORY  # GB
        self.available_storage = NODE_STORAGE  # GB
        self.jobs = []
        self.status = 'active'  # active or failed
        self.storage_system = Storage([])
        self.neighbors = []  # sending data to other nodes
        self.network = network  # network instance

    def add_neighbor(self, neighbor_node):
        self.neighbors.append(neighbor_node)

    def assign_job(self, job):
        if self.status != 'active':
            print(f"NODE {self.node_id} is not active")
            return False
        if job.memory_required > self.available_memory:
            print(f"NODE {self.node_id} does not have enough memory for Job {job.job_id}")
            return False
        self.jobs.append(job)
        self.available_memory -= job.memory_required
        job.status = 'running'
        threading.Thread(target=self.run_job, args=(job,)).start()
        return True

    def run_job(self, job):
        print(f"NODE {self.node_id} started Job {job.job_id}")
        start_time = time.time()
        while time.time() - start_time < job.runtime:
            time.sleep(1)
            if ENABLE_FAULTS and random.random() < FAULT_PROBABILITY:
                self.status = 'failed'
                job.status = 'failed'
                print(f"NODE {self.node_id} failed while running Job {job.job_id}")
                return
        job.status = 'completed'
        self.available_memory += job.memory_required
        self.jobs.remove(job)
        print(f"NODE {self.node_id} completed Job {job.job_id}")

        # simulate network communication after job completion
        self.send_job_result_to_neighbors(job)

    def send_job_result_to_neighbors(self, job):
        if self.neighbors:
            for neighbor in self.neighbors:
                # send job results to neighbors (using network simulator)
                self.network.send_data(15, self, neighbor)  # job result = 15MB

    def recover(self):
        if self.status == 'failed':
            self.status = 'active'
            print(f"NODE {self.node_id} has recovered")
