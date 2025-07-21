'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.kthvalue\ntorch.kthvalue(input, k, dim=None, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 4)
print(input)
print(torch.kthvalue(input, 2, dim=1, keepdim=False))
print(torch.kthvalue(input, 2, dim=1, keepdim=True))
print(torch.kthvalue(input, 2, dim=0, keepdim=False))
print(torch.kthvalue(input, 2, dim=0, keepdim=True))