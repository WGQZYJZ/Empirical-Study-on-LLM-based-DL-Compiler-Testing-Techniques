'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nan_to_num\ntorch.nan_to_num(input, nan=0.0, posinf=None, neginf=None, *, out=None)\n'
import torch
data = torch.randn(2, 2)
data[(0, 1)] = float('nan')
data[(1, 0)] = float('inf')
print(data)
print(torch.nan_to_num(data, nan=0.0, posinf=1.0, neginf=(- 1.0)))