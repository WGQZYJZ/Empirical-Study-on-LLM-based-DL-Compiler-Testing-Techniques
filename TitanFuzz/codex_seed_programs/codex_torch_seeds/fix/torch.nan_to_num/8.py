'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nan_to_num\ntorch.nan_to_num(input, nan=0.0, posinf=None, neginf=None, *, out=None)\n'
import torch
input = torch.randn(2, 3)
input[(0, 0)] = float('nan')
input[(1, 1)] = float('inf')
print(torch.nan_to_num(input))