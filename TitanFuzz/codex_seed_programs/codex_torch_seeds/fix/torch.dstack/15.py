'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dstack\ntorch.dstack(tensors, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
a = torch.rand(3, 5)
b = torch.rand(3, 5)
c = torch.rand(3, 5)
print('Task 3: Call the API torch.dstack')
out = torch.dstack((a, b, c))
print(out)
print(out.shape)