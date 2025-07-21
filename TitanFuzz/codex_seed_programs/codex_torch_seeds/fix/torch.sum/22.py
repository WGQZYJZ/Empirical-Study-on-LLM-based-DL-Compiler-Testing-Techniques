'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sum\ntorch.sum(input, dim, keepdim=False, *, dtype=None)\n'
import torch
input = torch.randn(3, 4, 5)
print(input)
print(torch.sum(input, dim=0))
print(torch.sum(input, dim=1))
print(torch.sum(input, dim=2))
print(torch.sum(input, dim=2, keepdim=True))
print(torch.sum(input, dim=2, keepdim=False))