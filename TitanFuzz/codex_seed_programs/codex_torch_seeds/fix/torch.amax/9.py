'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amax\ntorch.amax(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 4)
print(input)
print(torch.amax(input, dim=0))
print(torch.amax(input, dim=1))