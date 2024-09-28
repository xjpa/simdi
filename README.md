# about

project is inspired by https://read.seas.harvard.edu/cs260r/2022/project1/

system basically simulates a distributed infrastructure, nodes processing jobs wqith constraints like memory, CPU, etc. where jobs are assigned to nodes based on scheduling algorithms chosen by the user (Round Robin, FIFO). THere's also simulation for fault tolerance since nodes can fail during execution in the real world. Consistency models are also supported (Strong vs Eventual consistency).

# preview

```bash
---start simulation---
Node 0 started Job 6b171c04-a75e-4649-a198-5f5b29680516.
Node 0 started Job a2da53ae-afa5-4d37-9833-2f2b7082b13b.
Node 0 started Job 5135831c-9e16-44b1-b5f7-9d6c7ab79ec8.
Node 0 does not have enough memory for Job f5f714a7-8da5-441f-8853-4b72bfb23a4e.
Node 1 started Job f5f714a7-8da5-441f-8853-4b72bfb23a4e.Node 1 started Job 774f06f5-0440-439f-ba9a-33b91f546dc0.

Node 1 started Job b392c58f-5b78-41d4-ba69-017bece84242.
Node 1 started Job dd5ad57f-4d7f-499e-817b-8ec3c22c3669.
Node 1 does not have enough memory for Job d516672b-afe6-41cf-bfab-d5f18eb3bbba.
Node 2 started Job d516672b-afe6-41cf-bfab-d5f18eb3bbba.
Node 2 started Job 876a4258-ece0-4b98-a4e2-24c777599c54.
Node 2 does not have enough memory for Job 51c14e97-e48a-406c-9665-d9e5122d06d7.
Node 3 started Job 51c14e97-e48a-406c-9665-d9e5122d06d7.
Node 2 completed Job 876a4258-ece0-4b98-a4e2-24c777599c54.
transferring 15MB from NODE 2 to NODE 1 ✈️
data transfer from NODE 2 to NODE 1 ✅
transferring 15MB from NODE 2 to NODE 3 ✈️
data transfer from NODE 2 to NODE 3 ✅
Node 1 completed Job f5f714a7-8da5-441f-8853-4b72bfb23a4e.Node 1 completed Job 774f06f5-0440-439f-ba9a-33b91f546dc0.
transferring 15MB from NODE 1 to NODE 0 ✈️

transferring 15MB from NODE 1 to NODE 0 ✈️
Node 0 completed Job 5135831c-9e16-44b1-b5f7-9d6c7ab79ec8.
transferring 15MB from NODE 0 to NODE 1 ✈️
Node 1 completed Job dd5ad57f-4d7f-499e-817b-8ec3c22c3669.
transferring 15MB from NODE 1 to NODE 0 ✈️
data transfer from NODE 1 to NODE 0 ✅
transferring 15MB from NODE 1 to NODE 2 ✈️
data transfer from NODE 0 to NODE 1 ✅
data transfer from NODE 1 to NODE 0 ✅
data transfer from NODE 1 to NODE 0 ✅
transferring 15MB from NODE 1 to NODE 2 ✈️transferring 15MB from NODE 1 to NODE 2 ✈️

data transfer from NODE 1 to NODE 2 ✅data transfer from NODE 1 to NODE 2 ✅
data transfer from NODE 1 to NODE 2 ✅

Node 0 completed Job a2da53ae-afa5-4d37-9833-2f2b7082b13b.
Node 3 completed Job 51c14e97-e48a-406c-9665-d9e5122d06d7.
transferring 15MB from NODE 3 to NODE 2 ✈️
transferring 15MB from NODE 0 to NODE 1 ✈️
Node 0 completed Job 6b171c04-a75e-4649-a198-5f5b29680516.
transferring 15MB from NODE 0 to NODE 1 ✈️
data transfer from NODE 3 to NODE 2 ✅
transferring 15MB from NODE 3 to NODE 4 ✈️
data transfer from NODE 0 to NODE 1 ✅
data transfer from NODE 0 to NODE 1 ✅
data transfer from NODE 3 to NODE 4 ✅
Node 1 completed Job b392c58f-5b78-41d4-ba69-017bece84242.
transferring 15MB from NODE 1 to NODE 0 ✈️
Node 2 completed Job d516672b-afe6-41cf-bfab-d5f18eb3bbba.
transferring 15MB from NODE 2 to NODE 1 ✈️
data transfer from NODE 1 to NODE 0 ✅data transfer from NODE 2 to NODE 1 ✅
transferring 15MB from NODE 2 to NODE 3 ✈️

transferring 15MB from NODE 1 to NODE 2 ✈️
data transfer from NODE 2 to NODE 3 ✅
data transfer from NODE 1 to NODE 2 ✅
---simulation completed---
```