'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cat\ntorch.cat(tensors, dim=0, *, out=None)\n'
import torch
x = torch.rand(3, 3)
y = torch.rand(3, 3)
z = torch.rand(3, 3)
print(torch.cat((x, y, z), dim=1))