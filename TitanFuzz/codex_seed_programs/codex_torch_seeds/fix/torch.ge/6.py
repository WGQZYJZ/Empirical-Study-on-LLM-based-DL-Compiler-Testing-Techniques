'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ge\ntorch.ge(input, other, *, out=None)\n'
import torch
x = torch.randn(3, 4)
print(x)
y = torch.randn(3, 4)
print(y)
z = torch.ge(x, y)
print(z)
torch.ge(x, y, out=z)
print(z)