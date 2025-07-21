'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clamp\ntorch.clamp(input, min=None, max=None, *, out=None)\n'
import torch
import torch
x = torch.randn(10)
print(x)
print(torch.clamp(x, min=(- 0.5), max=0.5))