'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.polar\ntorch.polar(abs, angle, *, out=None)\n'
import torch
a = torch.randn(1, 3, 3)
print(a)
b = torch.polar(a, a)
print(b)