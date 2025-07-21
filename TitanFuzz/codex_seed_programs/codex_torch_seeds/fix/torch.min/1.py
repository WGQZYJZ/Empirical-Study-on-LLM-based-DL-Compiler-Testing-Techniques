'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.min\ntorch.min(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 5)
print(input)
print(torch.min(input, 1))
print(torch.min(input, 1)[0])
print(torch.min(input, 1)[1])
print(torch.min(input, 1, keepdim=True))
print(torch.min(input, 1, keepdim=True)[0])
print(torch.min(input, 1, keepdim=True)[1])