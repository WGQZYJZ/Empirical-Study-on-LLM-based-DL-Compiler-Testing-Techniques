'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.BatchSampler\ntorch.utils.data.BatchSampler(sampler, batch_size, drop_last)\n'
import torch
import numpy as np
import torch
data = np.random.randint(0, 100, size=100)
sampler = torch.utils.data.BatchSampler(data, batch_size=5, drop_last=False)
for i in sampler:
    print(i)
print(len(sampler))
print(type(sampler))