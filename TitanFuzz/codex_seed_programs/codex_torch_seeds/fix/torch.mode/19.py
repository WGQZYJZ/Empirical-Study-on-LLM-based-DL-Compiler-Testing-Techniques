'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mode\ntorch.mode(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(2, 3)
print(input)
print(torch.mode(input, dim=(- 1), keepdim=False, out=None))
print(torch.mode(input, dim=0, keepdim=False, out=None))
print(torch.mode(input, dim=(- 1), keepdim=True, out=None))