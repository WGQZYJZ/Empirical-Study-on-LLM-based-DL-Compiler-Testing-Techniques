'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logaddexp\ntorch.logaddexp(input, other, *, out=None)\n'
import torch
x = torch.rand(1)
y = torch.rand(1)
print(x)
print(y)
z = torch.logaddexp(x, y)
print(z)
z = torch.logaddexp(x, y, out=x)
print(z)
z = torch.logaddexp(x, y, out=y)
print(z)