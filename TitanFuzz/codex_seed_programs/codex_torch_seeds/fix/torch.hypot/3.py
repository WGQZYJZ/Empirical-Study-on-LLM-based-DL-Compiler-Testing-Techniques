'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hypot\ntorch.hypot(input, other, *, out=None)\n'
import torch
x = torch.rand(4)
y = torch.rand(4)
print(x)
print(y)
print(torch.hypot(x, y))