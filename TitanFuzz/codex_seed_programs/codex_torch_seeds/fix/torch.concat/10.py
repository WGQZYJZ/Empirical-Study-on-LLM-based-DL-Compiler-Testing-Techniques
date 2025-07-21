'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.concat\ntorch.concat(tensors, dim=0, *, out=None)\n'
import torch
x = torch.randn(2, 3)
y = torch.randn(2, 3)
z = torch.concat([x, y])
print(z)
z = torch.concat([x, y], dim=1)
print(z)