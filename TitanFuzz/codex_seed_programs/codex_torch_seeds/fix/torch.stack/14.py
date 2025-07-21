'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.stack\ntorch.stack(tensors, dim=0, *, out=None)\n'
import torch
a = torch.rand(2, 3)
b = torch.rand(2, 3)
c = torch.rand(2, 3)
d = torch.stack((a, b, c))
print(d.shape)
d = torch.stack((a, b, c), dim=1)
print(d.shape)