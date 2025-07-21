'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SubsetRandomSampler\ntorch.utils.data.SubsetRandomSampler(indices, generator=None)\n'
import torch
from torch.utils.data import SubsetRandomSampler
import torch
input_data = torch.arange(10)
print('input_data: {}'.format(input_data))
sampler = SubsetRandomSampler(list(range(3)))
print('sampler: {}'.format(sampler))
for idx in sampler:
    print('idx: {}'.format(idx))