'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.max\ntorch.max(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print(torch.max(input))
print(torch.max(input, dim=0))
print(torch.max(input, dim=1))
print(torch.max(input, dim=1, keepdim=True))
print(torch.argmax(input))
print(torch.argmax(input, dim=0))
print(torch.argmax(input, dim=1))
print(torch.argmax(input, dim=1, keepdim=True))