'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hstack\ntorch.hstack(tensors, *, out=None)\n'
import torch
x = torch.rand(5, 3)
y = torch.rand(5, 3)
z = torch.rand(5, 3)
print(torch.hstack((x, y, z)))
print(torch.hstack((x, y, z)).size())