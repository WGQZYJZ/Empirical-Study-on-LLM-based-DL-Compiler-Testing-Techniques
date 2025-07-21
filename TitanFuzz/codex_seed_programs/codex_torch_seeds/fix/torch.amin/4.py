'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amin\ntorch.amin(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print(input)
print(torch.amin(input, 1, keepdim=True))
print(torch.amin(input, 1, keepdim=False))
print(torch.amin(input, 0, keepdim=True))
print(torch.amin(input, 0, keepdim=False))