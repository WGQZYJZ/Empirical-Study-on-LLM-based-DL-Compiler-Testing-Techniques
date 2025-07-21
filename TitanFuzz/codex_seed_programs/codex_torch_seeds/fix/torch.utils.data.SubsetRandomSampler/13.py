'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SubsetRandomSampler\ntorch.utils.data.SubsetRandomSampler(indices, generator=None)\n'
import torch
from torch.utils.data import SubsetRandomSampler
import torch
input_data = torch.randint(0, 100, size=(100,))
indices = range(20, 100)
sampler = SubsetRandomSampler(indices)
for i in sampler:
    print(i)
sampler = torch.utils.data.RandomSampler(input_data, replacement=True)
for i in sampler:
    print(i)
sampler = torch.utils.data.RandomSampler(input_data, replacement=False)
for i in sampler:
    print(i)
sampler = torch.utils.data.RandomSampler(input_data, replacement=True, num_samples=5)
for i in sampler:
    print(i)