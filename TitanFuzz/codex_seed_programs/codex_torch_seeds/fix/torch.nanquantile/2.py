'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanquantile\ntorch.nanquantile(input, q, dim=None, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 4)
input[(1, 2)] = float('nan')
input[(2, 3)] = float('nan')
print(input)
print(torch.nanquantile(input, 0.5, dim=1))