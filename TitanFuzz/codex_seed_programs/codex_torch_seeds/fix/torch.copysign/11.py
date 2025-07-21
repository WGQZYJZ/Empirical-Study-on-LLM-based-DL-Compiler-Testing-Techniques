'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.copysign\ntorch.copysign(input, other, *, out=None)\n'
import torch
a = torch.randn(4)
print(a)
b = torch.randn(4)
print(b)
print(torch.copysign(a, b))