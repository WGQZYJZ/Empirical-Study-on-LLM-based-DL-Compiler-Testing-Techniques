'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mode\ntorch.mode(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
x = torch.randn(3, 4)
print(x)
print(torch.mode(x, dim=0))
print(torch.mode(x, dim=1))
print(torch.mode(x, dim=(- 1)))