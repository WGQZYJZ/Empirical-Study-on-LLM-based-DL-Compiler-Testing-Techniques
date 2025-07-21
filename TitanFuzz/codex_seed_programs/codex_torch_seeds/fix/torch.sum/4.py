'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sum\ntorch.sum(input, dim, keepdim=False, *, dtype=None)\n'
import torch
x = torch.randn(4, 4)
print(x)
print(torch.sum(x, dim=1))
print(torch.sum(x, dim=1, keepdim=True))
print(torch.sum(x, dim=0, keepdim=True))
print(torch.sum(x, dim=(- 1)))
print(torch.sum(x, dim=(- 1), keepdim=True))