'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ge\ntorch.ge(input, other, *, out=None)\n'
import torch
x = torch.randn(4, 4)
y = torch.randn(4, 4)
z = torch.ge(x, y)
print(x)
print(y)
print(z)