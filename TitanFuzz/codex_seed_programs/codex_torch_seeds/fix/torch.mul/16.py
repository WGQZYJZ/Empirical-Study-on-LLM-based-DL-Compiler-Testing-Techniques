'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mul\ntorch.mul(input, other, *, out=None)\n'
import torch
input = torch.randn(3, requires_grad=True)
other = torch.randn(3, requires_grad=True)
output = torch.mul(input, other)
print(output)