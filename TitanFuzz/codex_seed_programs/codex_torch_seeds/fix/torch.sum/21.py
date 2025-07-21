'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sum\ntorch.sum(input, dim, keepdim=False, *, dtype=None)\n'
import torch
input = torch.randn(10, 10)
output = torch.sum(input, dim=0)
print(output)
output = torch.sum(input, dim=1)
print(output)
output = torch.sum(input, dim=1, keepdim=True)
print(output)