'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanmean\ntorch.nanmean(input, dim=None, keepdim=False, *, dtype=None, out=None)\n'
import torch
input = torch.randn(3, 4, 5)
input[(1, 2, 3)] = float('nan')
print(input)
print(torch.nanmean(input, dim=0))
print(torch.nanmean(input, dim=1))
print(torch.nanmean(input, dim=2))