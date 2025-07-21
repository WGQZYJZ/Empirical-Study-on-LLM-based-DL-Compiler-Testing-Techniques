'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanquantile\ntorch.nanquantile(input, q, dim=None, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(4, 3)
print('input:', input)
q = torch.tensor([0.1, 0.5, 0.9])
output = torch.nanquantile(input, q)
print('output:', output)