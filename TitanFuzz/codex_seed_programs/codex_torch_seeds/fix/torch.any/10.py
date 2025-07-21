'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.any\ntorch.any(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print(input)
result = torch.any(input, dim=1)
print(result)
result = torch.any(input, dim=1, keepdim=True)
print(result)
result = torch.any(input, dim=(- 1))
print(result)
result = torch.any(input, dim=(- 1), keepdim=True)
print(result)