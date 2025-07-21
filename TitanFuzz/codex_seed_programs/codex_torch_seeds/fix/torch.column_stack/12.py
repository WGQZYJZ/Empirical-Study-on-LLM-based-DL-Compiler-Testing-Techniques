'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.column_stack\ntorch.column_stack(tensors, *, out=None)\n'
import torch
a = torch.rand(2, 3)
b = torch.rand(2, 3)
print(a)
print(b)
c = torch.column_stack((a, b))
print(c)
d = torch.cat((a, b), dim=1)
print(d)