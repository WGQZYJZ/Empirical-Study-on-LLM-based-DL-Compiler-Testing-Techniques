'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clamp\ntorch.clamp(input, min=None, max=None, *, out=None)\n'
import torch
x = torch.randn(1, 2, 3)
print(x)
y = torch.clamp(x, min=(- 0.5), max=0.5)
print(y)