'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_3d\ntorch.atleast_3d(*tensors)\n'
import torch
x = torch.tensor([1, 2, 3, 4], dtype=torch.float)
print(x)
y = torch.tensor([1, 2, 3, 4], dtype=torch.float)
print(y)
z = torch.tensor([1, 2, 3, 4], dtype=torch.float)
print(z)
print(torch.atleast_3d(x, y, z))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cat\ntorch.cat(seq, dim=0, out=None)\n'
import torch
x = torch.tensor([1, 2, 3, 4], dtype=torch.float)
print(x)
y = torch.tensor([5, 6, 7, 8], dtype=torch.float)
print(y)
z = torch.tensor([9, 10, 11, 12], dtype=torch.float)
print(z)