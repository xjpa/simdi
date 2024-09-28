# config.py

NUM_NODES = 5
NUM_JOBS = 10

NETWORK_LATENCY = 10  # milliseconds
NETWORK_BANDWIDTH = 100  # MB/s

NODE_CPU = 4  # cores
NODE_MEMORY = 8  # GB
NODE_STORAGE = 100  # GB

JOB_MIN_RUNTIME = 1  # seconds
JOB_MAX_RUNTIME = 5  # seconds
JOB_MIN_MEMORY = 1  # GB
JOB_MAX_MEMORY = 4  # GB
JOB_DATA_SIZE = 10  # MB per job

# round_robin, fifo, priority
SCHEDULING_ALGORITHM = 'round_robin'

# consistency model ('strong', 'eventual')
CONSISTENCY_MODEL = 'eventual'

# fault tolerance
ENABLE_FAULTS = False
FAULT_PROBABILITY = 0.1  # probability of node failure per job

# simulation time steps
TIME_STEP = 1  # second
