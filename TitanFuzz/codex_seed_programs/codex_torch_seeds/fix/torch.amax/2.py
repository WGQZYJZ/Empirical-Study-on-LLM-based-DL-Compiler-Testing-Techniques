'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amax\ntorch.amax(input, dim, keepdim=False, *, out=None)\n'
import torch
x = torch.randn(3, 4)
print(x)
print(torch.amax(x, dim=0))
print(torch.amax(x, dim=1))
print(torch.amax(x, dim=0, keepdim=True))
print(torch.amax(x, dim=1, keepdim=True))
print(torch.amax(x, dim=1, keepdim=True, out=torch.zeros_like(x)))