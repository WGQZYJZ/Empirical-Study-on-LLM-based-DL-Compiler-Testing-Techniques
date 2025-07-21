'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mul\ntorch.mul(input, other, *, out=None)\n'
import torch
x = torch.rand(5, 3)
y = torch.rand(5, 3)
print(x)
print(y)
print(torch.mul(x, y))