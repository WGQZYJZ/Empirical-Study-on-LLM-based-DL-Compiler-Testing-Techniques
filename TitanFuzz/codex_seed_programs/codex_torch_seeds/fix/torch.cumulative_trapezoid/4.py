'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumulative_trapezoid\ntorch.cumulative_trapezoid(y, x=None, *, dx=None, dim=-1)\n'
import torch
y = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=torch.float32)
print('y: ', y)
integral_y = torch.cumulative_trapezoid(y)
print('integral_y: ', integral_y)