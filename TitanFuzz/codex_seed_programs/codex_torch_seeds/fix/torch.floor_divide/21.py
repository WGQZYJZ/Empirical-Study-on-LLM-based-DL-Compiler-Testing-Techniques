'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor_divide\ntorch.floor_divide(input, other, *, out=None)\n'
import torch
input = torch.randn(1, 3)
other = torch.randn(1, 3)
print(input)
print(other)
print(torch.floor_divide(input, other))