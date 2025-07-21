'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.concat\ntorch.concat(tensors, dim=0, *, out=None)\n'
import torch
x = torch.rand(3, 4)
y = torch.rand(3, 4)
z = torch.rand(3, 4)
print(x)
print(y)
print(z)
print(torch.concat((x, y, z), 0))
print(torch.concat((x, y, z), 1))
print(torch.cat((x, y, z), 0))
print(torch.cat((x, y, z), 1))