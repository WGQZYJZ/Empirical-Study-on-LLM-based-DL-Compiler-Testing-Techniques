'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logaddexp\ntorch.logaddexp(input, other, *, out=None)\n'
import torch
a = torch.randn(4)
b = torch.randn(4)
print(a)
print(b)
print(torch.logaddexp(a, b))