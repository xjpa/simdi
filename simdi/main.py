# main.py

import time
from node import Node
from job import Job
from scheduler import Scheduler
from network import NetworkSimulator
from storage import Storage
from config import NUM_NODES, NUM_JOBS, ENABLE_FAULTS

def main():
    network = NetworkSimulator()

    # pass the network to each node
    nodes = [Node(node_id=i, network=network) for i in range(NUM_NODES)]
    scheduler = Scheduler(nodes)

    # connect nodes as neighbors for network communication
    for i in range(NUM_NODES):
        if i < NUM_NODES - 1:
            nodes[i].add_neighbor(nodes[i+1])  # connect node to the next node
            nodes[i+1].add_neighbor(nodes[i])  # connect the reverse

    jobs = [Job() for _ in range(NUM_JOBS)]
    for job in jobs:
        scheduler.add_job(job)

    # scheduling
    print("---start simulation---")
    while scheduler.queue or any(node.jobs for node in nodes):
        scheduler.schedule()
        time.sleep(1)
        if ENABLE_FAULTS:
            for node in nodes:
                if node.status == 'failed':
                    node.recover()

    print("---simulation completed---")

if __name__ == "__main__":
    main()
