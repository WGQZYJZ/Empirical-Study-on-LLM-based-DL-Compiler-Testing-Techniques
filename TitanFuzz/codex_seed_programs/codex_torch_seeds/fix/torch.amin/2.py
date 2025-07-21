'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amin\ntorch.amin(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 4)
print(torch.amin(input, dim=1))
print(torch.amin(input, dim=1, keepdim=True))
print(torch.amin(input, dim=0))
print(torch.amin(input, dim=0, keepdim=True))
print(torch.amin(input, dim=(- 1)))
print(torch.amin(input, dim=(- 1), keepdim=True))