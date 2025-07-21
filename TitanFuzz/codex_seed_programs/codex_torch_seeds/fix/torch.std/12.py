'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.std\ntorch.std(input, dim, unbiased, keepdim=False, *, out=None)\n'
import torch
x = torch.randn(2, 3)
print(x)
print(torch.std(x))
print(torch.std(x, dim=0))
print(torch.std(x, dim=1))
print(torch.std(x, dim=1, unbiased=False))
print(torch.std(x, unbiased=False))