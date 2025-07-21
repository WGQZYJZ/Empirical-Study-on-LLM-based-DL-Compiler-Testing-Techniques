'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vstack\ntorch.vstack(tensors, *, out=None)\n'
import torch
a = torch.rand(3, 1)
b = torch.rand(3, 1)
print(a)
print(b)
c = torch.vstack([a, b])
print(c)