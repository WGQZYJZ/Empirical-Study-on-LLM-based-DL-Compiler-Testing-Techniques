'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.igammac\ntorch.igammac(input, other, *, out=None)\n'
import torch
input = torch.rand(2, 3)
other = torch.rand(2, 3)
print(torch.igammac(input, other))