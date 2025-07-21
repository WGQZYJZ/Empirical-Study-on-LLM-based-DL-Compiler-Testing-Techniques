'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmod\ntorch.fmod(input, other, *, out=None)\n'
import torch
a = torch.randn(4)
print(a)
b = torch.randn(4)
print(b)
print(torch.fmod(a, b))