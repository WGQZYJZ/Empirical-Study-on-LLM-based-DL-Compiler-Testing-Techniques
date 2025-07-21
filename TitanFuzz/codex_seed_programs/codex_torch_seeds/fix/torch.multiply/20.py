'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.multiply\ntorch.multiply(input, other, *, out=None)\n'
import torch
a = torch.randn(2, 3)
b = torch.randn(2, 3)
print(a)
print(b)
print(torch.multiply(a, b))
print(torch.mul(a, b))