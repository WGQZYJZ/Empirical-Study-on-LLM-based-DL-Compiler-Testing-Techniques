'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.any\ntorch.any(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print('input = ', input)
print('torch.any(input) = ', torch.any(input))
print('torch.any(input, dim=0) = ', torch.any(input, dim=0))
print('torch.any(input, dim=1) = ', torch.any(input, dim=1))
print('torch.any(input, dim=0, keepdim=True) = ', torch.any(input, dim=0, keepdim=True))
print('torch.any(input, dim=1, keepdim=True) = ', torch.any(input, dim=1, keepdim=True))
'\nTask 4: Call the API torch.all\ntorch.all(input, dim, keepdim=False, *, out=None)\n'