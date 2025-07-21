'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clamp\ntorch.clamp(input, min=None, max=None, *, out=None)\n'
import torch
x = torch.randn(10, 10)
print(x)
y = torch.clamp(x, min=(- 0.5), max=0.5)
print(y)
y = torch.clamp_max(x, max=0.5)
print(y)
y = torch.clamp_min(x, min=(- 0.5))
print(y)
y = torch.clamp_max_(x, max=0.5)
print(y)
y = torch.clamp_min_(x, min=(- 0.5))
print(y)