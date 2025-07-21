'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SubsetRandomSampler\ntorch.utils.data.SubsetRandomSampler(indices, generator=None)\n'
import torch
from torch.utils.data import SubsetRandomSampler
import torch
input_data = list(range(10))
print(input_data)
sampler = SubsetRandomSampler(list(range(1, 10)))
print(sampler)
for i in sampler:
    print(i)