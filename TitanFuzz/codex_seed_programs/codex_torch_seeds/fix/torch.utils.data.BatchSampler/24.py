'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.BatchSampler\ntorch.utils.data.BatchSampler(sampler, batch_size, drop_last)\n'
import torch
from torch.utils.data import BatchSampler
data = torch.arange(0, 100)
batch_sampler = BatchSampler(sampler=data, batch_size=10, drop_last=False)
for batch in batch_sampler:
    print(batch)