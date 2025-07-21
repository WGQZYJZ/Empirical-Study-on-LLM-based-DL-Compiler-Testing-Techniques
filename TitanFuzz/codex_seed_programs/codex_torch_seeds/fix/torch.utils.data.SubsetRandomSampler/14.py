'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SubsetRandomSampler\ntorch.utils.data.SubsetRandomSampler(indices, generator=None)\n'
import torch
from torch.utils.data import SubsetRandomSampler
import torch
input_data = torch.arange(0, 100)
sampler = SubsetRandomSampler(indices=range(0, 5))
for i in sampler:
    print(input_data[i])