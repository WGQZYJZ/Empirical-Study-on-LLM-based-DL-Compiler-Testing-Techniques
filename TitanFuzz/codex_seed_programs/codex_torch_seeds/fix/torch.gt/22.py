'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gt\ntorch.gt(input, other, *, out=None)\n'
import torch
x = torch.randn(4, 4)
y = torch.randn(4, 4)
print(x)
print(y)
z = torch.gt(x, y)
print(z)