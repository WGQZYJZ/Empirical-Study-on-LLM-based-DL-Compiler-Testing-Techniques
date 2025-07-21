'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cross\ntorch.cross(input, other, dim=None, *, out=None)\n'
import torch
x = torch.randn(4, 3)
y = torch.randn(4, 3)
print(torch.cross(x, y, dim=1))
print(torch.cross(x, y, dim=1).shape)