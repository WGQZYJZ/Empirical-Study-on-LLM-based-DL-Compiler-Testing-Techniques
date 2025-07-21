'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanmean\ntorch.nanmean(input, dim=None, keepdim=False, *, dtype=None, out=None)\n'
import torch
import torch
input = torch.randn(3, 4)
input[(0, 0)] = float('nan')
input[(2, 3)] = float('nan')
print(input)
print(torch.nanmean(input))