'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmax\ntorch.fmax(input, other, *, out=None)\n'
import torch
a = torch.randn(4)
b = torch.randn(4)
c = torch.fmax(a, b)
print(c)
d = torch.fmax(a, b, out=c)
print(d)