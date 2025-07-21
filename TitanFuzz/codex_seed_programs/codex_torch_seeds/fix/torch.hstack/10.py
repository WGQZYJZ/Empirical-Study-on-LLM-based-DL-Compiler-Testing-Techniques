'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hstack\ntorch.hstack(tensors, *, out=None)\n'
import torch
import torch
x = torch.rand(2, 3)
y = torch.rand(2, 3)
z = torch.hstack((x, y))
print(z)
z = torch.zeros(2, 6)
torch.hstack((x, y), out=z)
print(z)
z = torch.hstack((x, y, x))
print(z)