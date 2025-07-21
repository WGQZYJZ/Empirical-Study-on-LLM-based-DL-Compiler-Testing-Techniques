'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.squeeze\ntorch.squeeze(input, dim=None, *, out=None)\n'
import torch
x = torch.randn(1, 3, 1, 1)
print(x)
y = torch.squeeze(x)
print(y)
y = torch.squeeze(x, dim=0)
print(y)
y = torch.squeeze(x, dim=2)
print(y)
y = torch.squeeze(x, dim=3)
print(y)