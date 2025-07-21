'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SubsetRandomSampler\ntorch.utils.data.SubsetRandomSampler(indices, generator=None)\n'
import torch
from torch.utils.data import SubsetRandomSampler
data = torch.randn(10)
print(data)
sampler = SubsetRandomSampler(indices=[1, 2, 3, 4, 5])
for i in sampler:
    print(i)