'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.var\ntorch.var(input, dim, unbiased, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(10, 5)
print(input)
print(torch.var(input))
print(torch.var(input, dim=0))
print(torch.var(input, dim=1))
print(torch.var(input, dim=1, unbiased=False))
print(torch.var(input, dim=1, keepdim=True))