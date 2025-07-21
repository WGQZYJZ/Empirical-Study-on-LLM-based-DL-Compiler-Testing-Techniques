'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumulative_trapezoid\ntorch.cumulative_trapezoid(y, x=None, *, dx=None, dim=-1)\n'
import torch
y = torch.randn(3, 4)
print('y = ', y)
result = torch.cumulative_trapezoid(y)
print('result = ', result)