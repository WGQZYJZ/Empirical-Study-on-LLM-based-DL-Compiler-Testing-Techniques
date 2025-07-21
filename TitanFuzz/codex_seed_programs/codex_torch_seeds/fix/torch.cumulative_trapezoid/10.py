'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumulative_trapezoid\ntorch.cumulative_trapezoid(y, x=None, *, dx=None, dim=-1)\n'
import torch
x = torch.arange(1, 5, dtype=torch.float)
y = torch.arange(1, 5, dtype=torch.float)
result = torch.cumulative_trapezoid(y, x=x)
print('result is: ', result)