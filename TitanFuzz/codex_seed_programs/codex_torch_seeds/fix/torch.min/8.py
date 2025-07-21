'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.min\ntorch.min(input, dim, keepdim=False, *, out=None)\n'
import torch
import numpy as np
a = torch.randn(3, 3)
print(a)
print(torch.min(a))
print(torch.min(a, dim=0))
print(torch.min(a, dim=1))
print(torch.min(a, dim=1, keepdim=True))
print(torch.max(a))
print(torch.max(a, dim=0))
print(torch.max(a, dim=1))
print(torch.max(a, dim=1, keepdim=True))
print(torch.argmin(a))
print(torch.argmin(a, dim=0))
print(torch.argmin(a, dim=1))
print(torch.argmax(a))
print(torch.argmax(a, dim=0))