'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mean\ntorch.mean(input, dim, keepdim=False, *, dtype=None)\n'
import torch
input = torch.randn(4, 4)
print(input)
mean = torch.mean(input)
print(mean)
mean = torch.mean(input, dim=0)
print(mean)