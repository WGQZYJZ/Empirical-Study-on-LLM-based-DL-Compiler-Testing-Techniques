'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clip\ntorch.clip(input, min=None, max=None, *, out=None)\n'
import torch
import numpy as np
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
x = torch.tensor([(- 2.0), (- 1.0), 0.0, 1.0, 2.0])
print('x =', x)
print('Task 3: Call the API torch.clip')
y = torch.clip(x, (- 1.0), 1.0)
print('y =', y)