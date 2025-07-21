'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cat\ntorch.cat(tensors, dim=0, *, out=None)\n'
import torch
import torch
x = torch.randn(3, 4)
y = torch.randn(3, 4)
z = torch.randn(3, 4)
x_cat = torch.cat((x, y, z), dim=0)
print(x_cat)