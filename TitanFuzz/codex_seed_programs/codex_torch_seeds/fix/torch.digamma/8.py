'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.digamma\ntorch.digamma(input, *, out=None)\n'
import torch
x = torch.randn(2, 3, 4)
print(x)
print(torch.digamma(x))