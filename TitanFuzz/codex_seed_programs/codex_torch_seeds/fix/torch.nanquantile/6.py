'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanquantile\ntorch.nanquantile(input, q, dim=None, keepdim=False, *, out=None)\n'
import numpy as np
import torch
import torch
input = torch.rand(4, 3)
print(input)
torch.nanquantile(input, q=0.5, dim=0, keepdim=False, out=None)
q = torch.tensor([0.25, 0.5, 0.75])
torch.nanquantile(input, q=q, dim=0, keepdim=False, out=None)
q = torch.tensor([0.25, 0.5, 0.75])
torch.nanquantile(input, q=q, dim=1, keepdim=False, out=None)