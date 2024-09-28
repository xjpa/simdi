# network.py

import time
from config import NETWORK_LATENCY, NETWORK_BANDWIDTH

class NetworkSimulator:
    def __init__(self, latency=NETWORK_LATENCY, bandwidth=NETWORK_BANDWIDTH):
        self.latency = latency  # milliseconds
        self.bandwidth = bandwidth  # MB/s

    def send_data(self, data_size, from_node, to_node):
        transfer_time = (data_size / self.bandwidth)  # seconds
        total_time = transfer_time + (self.latency / 1000)
        print(f"transferring {data_size}MB from NODE {from_node.node_id} to NODE {to_node.node_id} ✈️")
        time.sleep(total_time)
        print(f"data transfer from NODE {from_node.node_id} to NODE {to_node.node_id} ✅")
