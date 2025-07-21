'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sum\ntorch.sum(input, dim, keepdim=False, *, dtype=None)\n'
import torch
import torch
x = torch.rand(3, 3)
print('Input data: \n', x)
y = torch.sum(x, dim=1)
print('Output data: \n', y)
y = torch.sum(x, dim=1, keepdim=True)
print('Output data with keepdim=True: \n', y)