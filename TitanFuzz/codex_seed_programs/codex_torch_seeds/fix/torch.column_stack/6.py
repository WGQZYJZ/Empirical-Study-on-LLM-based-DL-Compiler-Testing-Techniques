'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.column_stack\ntorch.column_stack(tensors, *, out=None)\n'
import torch
import torch
a = torch.rand(3, 4)
b = torch.rand(3, 4)
print('a: ', a)
print('b: ', b)
c = torch.column_stack((a, b))
print('c: ', c)
d = torch.column_stack((a, b, a))
print('d: ', d)