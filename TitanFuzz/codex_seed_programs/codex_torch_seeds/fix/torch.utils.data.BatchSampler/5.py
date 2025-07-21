'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.BatchSampler\ntorch.utils.data.BatchSampler(sampler, batch_size, drop_last)\n'
import torch
import numpy as np
import torch
x = np.random.randn(100, 3, 32, 32)
y = np.random.randn(100)
sampler = torch.utils.data.SequentialSampler(range(len(x)))
batch_sampler = torch.utils.data.BatchSampler(sampler, batch_size=2, drop_last=False)
for indices in batch_sampler:
    print(indices)