'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.digamma\ntorch.special.digamma(input, *, out=None)\n'
import torch
input = torch.randn(1, 3)
print(input)
print(torch.special.digamma(input))