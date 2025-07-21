'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumulative_trapezoid\ntorch.cumulative_trapezoid(y, x=None, *, dx=None, dim=-1)\n'
import torch
y = torch.randn(10, 10)
import torch
y = torch.randn(10, 10)
torch.cumulative_trapezoid(y, dim=0)
torch.cumulative_trapezoid(y, dim=1)
torch.cumulative_trapezoid(y, x=torch.randn(10, 10), dim=1)