'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.less\ntorch.less(input, other, *, out=None)\n'
import torch
x = torch.randn(1, 3)
y = torch.randn(1, 3)
print(x)
print(y)
print(torch.less(x, y))
print(torch.less(x, y, out=x))
print(x)