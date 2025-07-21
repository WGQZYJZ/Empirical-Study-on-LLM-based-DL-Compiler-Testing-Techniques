'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.inner\ntorch.inner(input, other, *, out=None)\n'
import torch
input = torch.randn(3, 4)
print(input)
other = torch.randn(4)
print(other)
print(torch.inner(input, other))