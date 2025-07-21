'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dstack\ntorch.dstack(tensors, *, out=None)\n'
import torch
x = torch.rand(3, 4)
y = torch.rand(3, 4)
z = torch.rand(3, 4)
torch.dstack((x, y, z))
torch.dstack((x, y, z)).shape