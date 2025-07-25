'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.var\ntorch.var(input, dim, unbiased, keepdim=False, *, out=None)\n'
import torch
x = torch.rand(3, 3)
print(x)
print(torch.var(x))
print(torch.var(x, dim=0))
print(torch.var(x, dim=1))
print(torch.var(x, dim=0, unbiased=False))
print(torch.var(x, dim=1, unbiased=False))
print(torch.var(x, dim=0, unbiased=False, keepdim=True))
print(torch.var(x, dim=1, unbiased=False, keepdim=True))
print(torch.std(x))
print(torch.std(x, dim=0))
print(torch.std(x, dim=1))
print(torch.std(x, dim=0, unbiased=False))
print(torch.std(x, dim=1, unbiased=False))