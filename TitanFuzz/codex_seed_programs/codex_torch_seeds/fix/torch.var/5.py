'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.var\ntorch.var(input, dim, unbiased, keepdim=False, *, out=None)\n'
import torch
x = torch.Tensor([[1, 2], [3, 4]])
print(x)
print(torch.var(x, dim=0, unbiased=True))
print(torch.var(x, dim=0, unbiased=True, keepdim=True))
print(torch.var(x, dim=1, unbiased=True))
print(torch.var(x, dim=1, unbiased=True, keepdim=True))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mean\ntorch.mean(input, dim, keepdim=False, *, out=None)\n'
import torch
x = torch.Tensor([[1, 2], [3, 4]])
print(x)
print(torch.mean(x, dim=0, keepdim=True))
print(torch.mean(x, dim=1, keepdim=True))
print(torch.mean(x, dim=1, keepdim=False))