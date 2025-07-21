'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.var\ntorch.var(input, dim, unbiased, keepdim=False, *, out=None)\n'
import torch
x = torch.randn(3, 3)
print(x)
print(torch.var(x))
print(torch.var(x, dim=0))
print(torch.var(x, dim=1))
print(torch.var(x, dim=1, unbiased=False))
print(torch.var(x, dim=1, keepdim=True))
print(torch.var(x, dim=1, keepdim=True, out=torch.FloatTensor([1, 2, 3])))
print(torch.var(x, dim=1, keepdim=True, out=torch.FloatTensor([1, 2, 3])))