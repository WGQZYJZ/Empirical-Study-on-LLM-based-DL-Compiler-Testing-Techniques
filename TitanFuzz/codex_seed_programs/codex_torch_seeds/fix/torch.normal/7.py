'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.normal\ntorch.normal(mean, std, size, *, out=None)\n'
import torch
x = torch.randn(3, 4)
print(x)
y = torch.normal(0, 1, (3, 4))
print(y)
z = torch.normal(0, 1, (3, 4), out=x)
print(z)