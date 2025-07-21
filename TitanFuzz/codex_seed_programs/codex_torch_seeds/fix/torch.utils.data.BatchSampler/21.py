'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.BatchSampler\ntorch.utils.data.BatchSampler(sampler, batch_size, drop_last)\n'
import torch
import numpy as np
data = np.arange(100)
sampler = torch.utils.data.BatchSampler(data, 5, drop_last=True)
for i in sampler:
    print(i)