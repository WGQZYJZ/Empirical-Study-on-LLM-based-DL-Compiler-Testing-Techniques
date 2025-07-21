'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mul\ntorch.mul(input, other, *, out=None)\n'
import torch
x = torch.rand(3, 4)
y = torch.rand(3, 4)
z = torch.mul(x, y)
print(z)