'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.le\ntorch.le(input, other, *, out=None)\n'
import torch
input = torch.randn(2, 2)
other = torch.randn(2, 2)
output = torch.le(input, other)
print(output)
output = torch.le(input, other, out=None)
print(output)