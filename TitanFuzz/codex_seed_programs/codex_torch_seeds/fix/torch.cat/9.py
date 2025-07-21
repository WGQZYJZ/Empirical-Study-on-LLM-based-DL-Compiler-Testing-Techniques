'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cat\ntorch.cat(tensors, dim=0, *, out=None)\n'
import torch
x = torch.rand(2, 3)
y = torch.rand(2, 3)
z = torch.rand(2, 3)
print(x)
print(y)
print(z)
w = torch.cat((x, y, z), dim=0)
print(w)
'\nTask 4: Call the API torch.stack\ntorch.stack(tensors, dim=0, *, out=None)\n'
import torch
x = torch.rand(2, 3)
y = torch.rand(2, 3)
z = torch.rand(2, 3)
print(x)
print(y)
print(z)
w = torch.stack((x, y, z), dim=0)
print(w)
'\nTask 5: Call the API torch.chunk\ntorch.chunk(tensor, chunks, dim=0)\n'
import torch
x = torch.rand(2, 3)
print(x)