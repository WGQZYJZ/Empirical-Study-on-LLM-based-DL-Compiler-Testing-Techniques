'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.min\ntorch.min(input, dim, keepdim=False, *, out=None)\n'
import torch
x = torch.randn(3, 4)
print(x)
print(torch.min(x, dim=0))
print(torch.min(x, dim=1))
print(torch.min(x, dim=0, keepdim=True))
print(torch.min(x, dim=1, keepdim=True))