'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clamp\ntorch.clamp(input, min=None, max=None, *, out=None)\n'
import torch
a = torch.randn(3, 3)
print(a)
b = torch.clamp(a, min=0, max=1)
print(b)