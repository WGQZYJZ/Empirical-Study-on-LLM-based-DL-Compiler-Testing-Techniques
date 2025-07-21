'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumulative_trapezoid\ntorch.cumulative_trapezoid(y, x=None, *, dx=None, dim=-1)\n'
import torch
y = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
cum_trapz = torch.cumulative_trapezoid(y, x)
print(cum_trapz)