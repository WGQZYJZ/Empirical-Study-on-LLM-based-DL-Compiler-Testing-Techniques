'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.RandomSampler\ntorch.utils.data.RandomSampler(data_source, replacement=False, num_samples=None, generator=None)\n'
import torch
import numpy as np
sampler = torch.utils.data.RandomSampler(np.arange(10))
batch_sampler = torch.utils.data.BatchSampler(sampler, batch_size=3, drop_last=False)
for batch in batch_sampler:
    print(batch)
for batch in batch_sampler:
    print(batch)