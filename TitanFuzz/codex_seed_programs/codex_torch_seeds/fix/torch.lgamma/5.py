'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lgamma\ntorch.lgamma(input, *, out=None)\n'
import torch
a = torch.randn(4, 4)
print(a)
b = torch.lgamma(a)
print(b)