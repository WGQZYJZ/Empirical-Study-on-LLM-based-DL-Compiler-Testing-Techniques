'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.min\ntorch.min(input, dim, keepdim=False, *, out=None)\n'
import torch
import torch
input = torch.randn(2, 3, 4)
print(input)
print(torch.min(input, dim=1))
print(torch.min(input, dim=0))
print(torch.min(input, dim=2))