'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.row_stack\ntorch.row_stack(tensors, *, out=None)\n'
import torch
x = torch.rand(4, 2)
y = torch.rand(4, 2)
z = torch.rand(4, 2)
print(torch.row_stack((x, y, z)))
'\nTask 4: Call the API torch.cat\ntorch.cat(tensors, dim=0, out=None)\n'
print(torch.cat((x, y, z), dim=0))