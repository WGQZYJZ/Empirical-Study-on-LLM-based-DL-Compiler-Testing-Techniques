'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nansum\ntorch.nansum(input, dim, keepdim=False, *, dtype=None)\n'
import torch
input = torch.randn(3, 3)
input[(1, 1)] = float('nan')
print(input)
print(torch.nansum(input, dim=1))
print(torch.nansum(input, dim=1, keepdim=True))
print(torch.nansum(input, dim=1, keepdim=True).shape)