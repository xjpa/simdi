# storage.py

from config import CONSISTENCY_MODEL

class Storage:
    def __init__(self, nodes):
        self.nodes = nodes
        self.data = {}

    def write_data(self, key, value, node):
        if CONSISTENCY_MODEL == 'strong':
            for n in self.nodes:
                n.storage_system.data[key] = value
        elif CONSISTENCY_MODEL == 'eventual':
            node.storage_system.data[key] = value
        print(f"data '{key}':'{value}' written to NODE {node.node_id}")

    def read_data(self, key, node):
        value = node.storage_system.data.get(key, None)
        print(f"data '{key}':'{value}' read from NODE {node.node_id}")
        return value
