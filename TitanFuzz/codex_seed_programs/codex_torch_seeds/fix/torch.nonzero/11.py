'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nonzero\ntorch.nonzero(input, *, out=None, as_tuple=False)\n'
import torch
input = torch.randn(4, 4)
input[(0, 0)] = 0
input[(1, 1)] = 0
input[(2, 2)] = 0
input[(3, 3)] = 0
print(torch.nonzero(input))