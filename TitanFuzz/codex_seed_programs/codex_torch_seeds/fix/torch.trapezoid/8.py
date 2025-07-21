'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.trapezoid\ntorch.trapezoid(y, x=None, *, dx=None, dim=- 1)\n'
import torch
y = torch.rand(5, 4, dtype=torch.float)
print('Input data: y = ', y)
print('Output data: ', torch.trapezoid(y))