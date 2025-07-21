'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mul\ntorch.mul(input, other, *, out=None)\n'
import torch
a = torch.randn(3, 3)
b = torch.randn(3, 3)
c = torch.mul(a, b)
print(c)