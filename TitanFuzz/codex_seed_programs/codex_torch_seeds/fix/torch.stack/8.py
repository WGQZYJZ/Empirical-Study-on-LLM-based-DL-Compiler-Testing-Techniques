'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.stack\ntorch.stack(tensors, dim=0, *, out=None)\n'
import torch
a = torch.rand(2, 3)
b = torch.rand(2, 3)
c = torch.stack([a, b], dim=0)
print(c)
print(c.shape)