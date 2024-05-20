import sys
import os

# for the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from simdi.simulation.node import Node
from simdi.simulation.network import Network
from simdi.simulation.simulation_engine import SimulationEngine

def main():
    engine = SimulationEngine()
    network = Network(engine)

    node_a = Node('A')
    node_b = Node('B')
    node_c = Node('C')

    network.add_node(node_a)
    network.add_node(node_b)
    network.add_node(node_c)

    network.connect_nodes('A', 'B')
    network.connect_nodes('A', 'C')
    network.connect_nodes('B', 'C')

    node_a.send_message("Hello from A", network)
    node_b.send_message("Hello from B", network)
    node_c.send_message("Hello from C", network)

    engine.run()

if __name__ == "__main__":
    main()
