'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor_divide\ntorch.floor_divide(input, other, *, out=None)\n'
import torch
x = torch.randn(3, 3)
y = torch.randn(3, 3)
print(x)
print(y)
print(torch.floor_divide(x, y))