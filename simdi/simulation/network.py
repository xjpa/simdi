from .event import Event
from .simulation_engine import SimulationEngine

class Network:
    def __init__(self, engine):
        self.engine = engine
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.node_id] = node

    def connect_nodes(self, node1_id, node2_id):
        self.nodes[node1_id].add_neighbor(node2_id)
        self.nodes[node2_id].add_neighbor(node1_id)

    def schedule_message(self, from_node, to_node, message):
        def message_action():
            print(f"Message from {from_node} to {to_node}: {message}")
        
        # added a small delay for simulation purposes
        self.engine.schedule_event(Event(self.engine.current_time + 1, message_action))
