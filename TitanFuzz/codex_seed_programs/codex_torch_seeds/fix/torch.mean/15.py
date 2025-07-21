'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mean\ntorch.mean(input, dim, keepdim=False, *, dtype=None)\n'
import torch
input = torch.randn(4, 4)
print(torch.mean(input))
print(torch.mean(input, 1))
print(torch.mean(input, 1, keepdim=True))
print(torch.mean(input, 1, keepdim=True).shape)
print(torch.mean(input, 1, keepdim=False))
print(torch.mean(input, 1, keepdim=False).shape)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sum\ntorch.sum(input, dim, keepdim=False, *, dtype=None)\n'
import torch
input = torch.randn(4, 4)
print(torch.sum(input))