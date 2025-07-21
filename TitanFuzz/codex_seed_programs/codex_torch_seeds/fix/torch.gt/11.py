'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gt\ntorch.gt(input, other, *, out=None)\n'
import torch
input = torch.randn(3, 3)
other = torch.randn(3, 3)
print(input)
print(other)
print(torch.gt(input, other))