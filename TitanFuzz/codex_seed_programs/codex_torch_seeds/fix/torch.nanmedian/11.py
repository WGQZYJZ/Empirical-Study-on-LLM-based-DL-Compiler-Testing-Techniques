'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanmedian\ntorch.nanmedian(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 4)
input[(1, 2)] = float('nan')
input[(2, 3)] = float('nan')
output = torch.nanmedian(input, dim=(- 1), keepdim=False, out=None)
print(output)