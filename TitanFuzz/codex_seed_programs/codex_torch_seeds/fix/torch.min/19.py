'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.min\ntorch.min(input, dim, keepdim=False, *, out=None)\n'
import torch
x = torch.randn(4, 4)
print(torch.min(x, 1))
print(torch.min(x, 1, keepdim=True))
print(torch.min(x, 1, keepdim=True)[0])
print(torch.min(x, 1, keepdim=True)[1])
print(torch.min(x, 0))
print(torch.min(x, 0, keepdim=True))
print(torch.min(x, 0, keepdim=True)[0])
print(torch.min(x, 0, keepdim=True)[1])