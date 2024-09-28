# scheduler.py

from collections import deque
from config import SCHEDULING_ALGORITHM

class Scheduler:
    def __init__(self, nodes):
        self.nodes = nodes
        self.queue = deque()
        self.current_node_index = 0

    def add_job(self, job):
        self.queue.append(job)

    def schedule(self):
        if SCHEDULING_ALGORITHM == 'round_robin':
            self.round_robin()
        elif SCHEDULING_ALGORITHM == 'fifo':
            self.fifo()
        else:
            print(f"scheduling algorithm '{SCHEDULING_ALGORITHM}' not implemented")

    def round_robin(self):
        while self.queue:
            job = self.queue.popleft()
            assigned = False
            attempts = 0
            while not assigned and attempts < len(self.nodes):
                node = self.nodes[self.current_node_index]
                if node.assign_job(job):
                    assigned = True
                else:
                    self.current_node_index = (self.current_node_index + 1) % len(self.nodes)
                    attempts += 1
            if not assigned:
                print(f"job {job.job_id} could not be assigned. RE-QUEUEING")
                self.queue.append(job)
                break  # to prevent infinite loop

    def fifo(self):
        while self.queue:
            job = self.queue.popleft()
            for node in self.nodes:
                if node.assign_job(job):
                    break
            else:
                print(f"job {job.job_id} could not be assigned. RE-QUEUEING")
                self.queue.appendleft(job)
                break  # to prevent infinite loop
