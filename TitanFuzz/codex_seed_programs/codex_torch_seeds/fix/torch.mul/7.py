'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mul\ntorch.mul(input, other, *, out=None)\n'
import torch
input = torch.randn(2, 3)
other = torch.randn(2, 3)
output = torch.mul(input, other)
print(output)
output = torch.empty(2, 3)
torch.mul(input, other, out=output)
print(output)