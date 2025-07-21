'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mean\ntorch.mean(input, dim, keepdim=False, *, dtype=None)\n'
import torch
input = torch.randn(5, 3, 4)
print(input)
print(input.size())
mean = torch.mean(input, dim=1)
print(mean)
print(mean.size())
mean = torch.mean(input, dim=1, keepdim=True)
print(mean)
print(mean.size())
mean = torch.mean(input, dim=1, keepdim=True, dtype=torch.float32)
print(mean)
print(mean.size())