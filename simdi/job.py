# job.py

import uuid
import random
from config import JOB_MIN_RUNTIME, JOB_MAX_RUNTIME, JOB_MIN_MEMORY, JOB_MAX_MEMORY, JOB_DATA_SIZE

class Job:
    def __init__(self, job_id=None):
        self.job_id = job_id or str(uuid.uuid4())
        self.runtime = random.uniform(JOB_MIN_RUNTIME, JOB_MAX_RUNTIME)
        self.memory_required = random.uniform(JOB_MIN_MEMORY, JOB_MAX_MEMORY)
        self.data_size = JOB_DATA_SIZE  # MB
        self.dependencies = []  # list of job_ids that this job depends on
        self.status = 'pending'  # other stuff: pending, running, completed, failed

    def __repr__(self):
        return f"<Job {self.job_id} | Runtime: {self.runtime:.2f}s | Memory: {self.memory_required:.2f}GB>"
