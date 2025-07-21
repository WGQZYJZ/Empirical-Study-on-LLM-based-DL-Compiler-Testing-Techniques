'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.igammac\ntorch.igammac(input, other, *, out=None)\n'
import torch
input = torch.rand(1, 1)
other = torch.rand(1, 1)
out = torch.igammac(input, other)
print(out)