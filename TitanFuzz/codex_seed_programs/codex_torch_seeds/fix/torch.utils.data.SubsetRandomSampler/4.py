'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.SubsetRandomSampler\ntorch.utils.data.SubsetRandomSampler(indices, generator=None)\n'
import torch
import numpy as np
from torch.utils.data import SubsetRandomSampler
data = np.arange(100)
print(data)
sampler = SubsetRandomSampler(indices=list(range(0, 20, 2)))
print(sampler)
for i in sampler:
    print(i)