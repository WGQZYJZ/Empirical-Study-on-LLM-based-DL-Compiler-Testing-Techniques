'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.BatchSampler\ntorch.utils.data.BatchSampler(sampler, batch_size, drop_last)\n'
import torch
from torch.utils.data import BatchSampler, SubsetRandomSampler
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print('Task 3: Call the API torch.utils.data.BatchSampler')
batch_size = 4
data_sampler = SubsetRandomSampler(data)
batch_sampler = BatchSampler(data_sampler, batch_size, drop_last=True)
for (i, batch) in enumerate(batch_sampler):
    print(i, batch)