'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.le\ntorch.le(input, other, *, out=None)\n'
import torch
import numpy as np
print('Task 1: import PyTorch')
print()
print('Task 2: Generate input data')
input = torch.randn(3, 3)
print('input = ', input)
print()
print('Task 3: Call the API torch.le')
result = torch.le(input, torch.randn(3, 3))
print('result = ', result)
print()