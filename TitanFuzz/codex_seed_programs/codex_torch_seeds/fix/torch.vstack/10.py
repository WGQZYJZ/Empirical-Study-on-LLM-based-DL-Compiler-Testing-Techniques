'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vstack\ntorch.vstack(tensors, *, out=None)\n'
import torch
x = torch.rand(2, 3)
y = torch.rand(2, 3)
z = torch.vstack((x, y))
print(z)
z = torch.cat((x, y))
print(z)
z = torch.stack((x, y))
print(z)