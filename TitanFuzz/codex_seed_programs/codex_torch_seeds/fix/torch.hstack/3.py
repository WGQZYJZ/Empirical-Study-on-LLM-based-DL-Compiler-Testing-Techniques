'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hstack\ntorch.hstack(tensors, *, out=None)\n'
import torch
a = torch.rand(3, 4)
b = torch.rand(3, 4)
c = torch.rand(3, 4)
print(a)
print(b)
print(c)
print(torch.hstack((a, b, c)))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vstack\ntorch.vstack(tensors, *, out=None)\n'
import torch
a = torch.rand(3, 4)
b = torch.rand(3, 4)
c = torch.rand(3, 4)
print(a)
print(b)
print(c)
print(torch.vstack((a, b, c)))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.stack\ntorch.stack(tensors, dim=0, out=None)\n'
import torch
a = torch.rand(3, 4)
b