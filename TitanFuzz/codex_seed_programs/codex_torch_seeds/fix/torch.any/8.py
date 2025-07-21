'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.any\ntorch.any(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print(input)
print(torch.any((input > 0.5)))
print(torch.any((input > 0.5), dim=0))
print(torch.any((input > 0.5), dim=1))
print(torch.any((input > 0.5), dim=1, keepdim=True))
print(torch.any((input > 0.5), dim=(- 1)))
print(torch.any((input > 0.5), dim=(- 1), keepdim=True))