'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanquantile\ntorch.nanquantile(input, q, dim=None, keepdim=False, *, out=None)\n'
import torch
input = torch.rand(3, 3)
input[(0, 0)] = float('nan')
input[(0, 1)] = float('nan')
input[(2, 2)] = float('nan')
q = torch.tensor([0.25, 0.5, 0.75])
print(torch.nanquantile(input, q, dim=0))
print(torch.nanquantile(input, q, dim=1))