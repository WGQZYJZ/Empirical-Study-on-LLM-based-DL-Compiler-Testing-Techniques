'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.median\ntorch.median(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
import numpy as np
from numpy.random import randint
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
data = randint(0, 100, (2, 3))
print('Input data:\n', data)
print('Task 3: Call the API torch.median')
tensor = torch.from_numpy(data)
print('Tensor:\n', tensor)
median = torch.median(tensor, dim=1)
print('Median: ', median)