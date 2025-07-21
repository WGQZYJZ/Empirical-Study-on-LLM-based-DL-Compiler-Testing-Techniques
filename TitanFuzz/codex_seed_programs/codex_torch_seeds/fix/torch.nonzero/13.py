'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nonzero\ntorch.nonzero(input, *, out=None, as_tuple=False)\n'
import torch
input = torch.randn(3, 4)
print(input)
indices = torch.nonzero(input)
print(indices)
indices = torch.nonzero(input, as_tuple=True)
print(indices)