'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nan_to_num\ntorch.nan_to_num(input, nan=0.0, posinf=None, neginf=None, *, out=None)\n'
import torch
x = torch.tensor([[1, 2, 3], [float('nan'), float('-inf'), float('inf')]])
print(x)
print(torch.nan_to_num(x, nan=0))
print(torch.nan_to_num(x, nan=0, posinf=1, neginf=(- 1)))