'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.equal\ntorch.equal(input, other)\n'
import torch
import numpy as np
x = torch.randn(3, 3)
y = torch.randn(3, 3)
z = torch.equal(x, y)
print('x: ', x)
print('y: ', y)
print('z: ', z)