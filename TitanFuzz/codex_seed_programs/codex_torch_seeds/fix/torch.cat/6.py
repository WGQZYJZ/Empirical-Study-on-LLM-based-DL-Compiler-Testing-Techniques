'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cat\ntorch.cat(tensors, dim=0, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
x = torch.randn(4, 5)
y = torch.randn(4, 5)
z = torch.randn(4, 5)
print('Task 3: Call the API torch.cat')
print(torch.cat((x, y, z), dim=0).size())
print(torch.cat((x, y, z), dim=1).size())