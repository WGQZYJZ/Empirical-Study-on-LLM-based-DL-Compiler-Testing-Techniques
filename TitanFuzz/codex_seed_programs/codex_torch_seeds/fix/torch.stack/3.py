'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.stack\ntorch.stack(tensors, dim=0, *, out=None)\n'
import torch
x = torch.rand(3, 3)
y = torch.rand(3, 3)
z = torch.rand(3, 3)
print(torch.stack([x, y, z]))
print(torch.stack([x, y, z], dim=1))
print(torch.stack([x, y, z], dim=2))