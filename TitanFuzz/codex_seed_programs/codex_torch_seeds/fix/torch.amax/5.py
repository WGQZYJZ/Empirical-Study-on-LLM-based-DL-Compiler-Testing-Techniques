'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amax\ntorch.amax(input, dim, keepdim=False, *, out=None)\n'
import torch
a = torch.rand(3, 4)
print(a)
print(torch.amax(a, dim=1))
print(torch.amax(a, dim=0))
print(torch.amax(a, dim=1, keepdim=True))
print(torch.amax(a, dim=0, keepdim=True))