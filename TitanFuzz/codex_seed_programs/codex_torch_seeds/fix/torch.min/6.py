'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.min\ntorch.min(input, dim, keepdim=False, *, out=None)\n'
import torch
x = torch.randn(2, 3)
print(x)
print(torch.min(x))
print(torch.min(x, dim=0))
print(torch.min(x, dim=1))
print(torch.min(x, dim=1, keepdim=True))
print(torch.min(x, dim=1, keepdim=True)[0])
print(torch.min(x, dim=1, keepdim=True)[0].size())
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.max\ntorch.max(input, dim, keepdim=False, *, out=None)\n'
import torch
x = torch.randn(2, 3)
print(x)
print(torch.max(x))
print(torch.max(x, dim=0))
print(torch.max(x, dim=1))