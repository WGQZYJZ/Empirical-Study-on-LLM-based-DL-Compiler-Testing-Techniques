'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.median\ntorch.median(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(2, 3, 4)
print(input)
print(torch.median(input, dim=(- 1)))
print(torch.median(input, dim=0))
print(torch.median(input, dim=1))
print(torch.median(input, dim=2))
print(torch.median(input, dim=(- 1), keepdim=True))
print(torch.median(input, dim=(- 1), keepdim=False))