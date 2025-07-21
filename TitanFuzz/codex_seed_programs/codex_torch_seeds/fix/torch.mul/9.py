'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mul\ntorch.mul(input, other, *, out=None)\n'
import torch
a = torch.randn(5, 5)
b = torch.randn(5, 5)
print(torch.mul(a, b))
print(a.mul(b))