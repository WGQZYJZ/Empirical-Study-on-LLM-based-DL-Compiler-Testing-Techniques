'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.var\ntorch.var(input, dim, unbiased, keepdim=False, *, out=None)\n'
import torch
x = torch.tensor([1.0, (- 1.0), 1, (- 1)])
print(torch.var(x, unbiased=False))
print(torch.var(x, unbiased=True))
x = torch.tensor([[1.0, (- 1.0), 1, (- 1)], [1.0, (- 1.0), 1, (- 1)]])
print(torch.var(x, dim=0, unbiased=False))
print(torch.var(x, dim=0, unbiased=True))
print(torch.var(x, dim=1, unbiased=False))
print(torch.var(x, dim=1, unbiased=True))
print(torch.var(x, dim=1, keepdim=True, unbiased=False))
print(torch.var(x, dim=1, keepdim=True, unbiased=True))