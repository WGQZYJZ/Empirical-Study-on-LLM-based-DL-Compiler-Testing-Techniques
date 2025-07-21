'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanquantile\ntorch.nanquantile(input, q, dim=None, keepdim=False, *, out=None)\n'
import torch
input = torch.rand(100, 100)
input[0, :] = float('nan')
quantile = torch.nanquantile(input, q=0.5, dim=0, keepdim=False)
print(quantile)