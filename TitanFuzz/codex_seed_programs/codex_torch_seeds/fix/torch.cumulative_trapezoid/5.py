'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumulative_trapezoid\ntorch.cumulative_trapezoid(y, x=None, *, dx=None, dim=-1)\n'
import torch
import torch
y = torch.rand(3, 5)
torch.cumulative_trapezoid(y)
torch.cumulative_trapezoid(y, dim=0)
torch.cumulative_trapezoid(y, dim=1)
torch.cumulative_trapezoid(y, dim=(- 1))
torch.cumulative_trapezoid(y, dim=(- 2))