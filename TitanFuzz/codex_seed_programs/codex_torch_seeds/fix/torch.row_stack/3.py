'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.row_stack\ntorch.row_stack(tensors, *, out=None)\n'
import torch
a = torch.randn(2, 3)
b = torch.randn(2, 3)
print('a: ', a)
print('b: ', b)
c = torch.row_stack((a, b))
print('c: ', c)