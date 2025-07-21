'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.std\ntorch.std(input, dim, unbiased, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print(input)
print(torch.std(input, dim=0))
print(torch.std(input, dim=1))
print(torch.std(input, dim=0, unbiased=False))
print(torch.std(input, dim=1, unbiased=False))
print(torch.std(input, dim=0, unbiased=False, keepdim=True))
print(torch.std(input, dim=1, unbiased=False, keepdim=True))
print(torch.std(input, dim=0, unbiased=False, keepdim=True, out=torch.empty(3)))
print(torch.std(input, dim=1, unbiased=False, keepdim=True, out=torch.empty(3)))