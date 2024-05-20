class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def send_message(self, message, network):
        for neighbor in self.neighbors:
            network.schedule_message(self.node_id, neighbor, message)
