'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SubsetRandomSampler\ntorch.utils.data.SubsetRandomSampler(indices, generator=None)\n'
import torch
from torch.utils.data import DataLoader, SubsetRandomSampler
import torch
from torch.utils.data import DataLoader, SubsetRandomSampler
input_data = list(range(10))
sampler = SubsetRandomSampler(input_data)
print('The result of SubsetRandomSampler is: {}'.format(sampler))
print('The type of sampler is: {}'.format(type(sampler)))
print('The length of sampler is: {}'.format(len(sampler)))
print('The result of sampler.__iter__() is: {}'.format(sampler.__iter__()))