'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sum\ntorch.sum(input, dim, keepdim=False, *, dtype=None)\n'
import torch
input = torch.randn(3, 2)
print(input)
sum = torch.sum(input, dim=1)
print(sum)
sum = torch.sum(input, dim=1, keepdim=True)
print(sum)
sum = torch.sum(input, dim=1, keepdim=True, dtype=torch.float)
print(sum)