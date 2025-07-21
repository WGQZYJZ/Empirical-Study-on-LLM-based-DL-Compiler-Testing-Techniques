'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dstack\ntorch.dstack(tensors, *, out=None)\n'
import torch
x = torch.randn(2, 3, 4)
y = torch.randn(2, 3, 4)
z = torch.randn(2, 3, 4)
print(torch.dstack((x, y, z)).shape)
print(torch.dstack((x, y, z)))