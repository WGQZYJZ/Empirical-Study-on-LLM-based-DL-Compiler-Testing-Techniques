'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hstack\ntorch.hstack(tensors, *, out=None)\n'
import torch
a = torch.rand(2, 3)
b = torch.rand(2, 3)
print(a)
print(b)
c = torch.hstack((a, b))
print(c)