'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nonzero\ntorch.nonzero(input, *, out=None, as_tuple=False)\n'
import torch
input = torch.randn(3, 4)
print(input)
output = torch.nonzero(input)
print(output)