'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.take\ntorch.take(input, index)\n'
import torch
import numpy as np
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(3, 5)
index = torch.tensor([0, 4])
print('Task 3: Call the API torch.take')
print('torch.take(input, index)')
print(torch.take(input, index))