'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matmul\ntorch.linalg.matmul(input, other, *, out=None)\n'
import torch
a = torch.rand(5, 3)
print('a: ', a)
b = torch.rand(3, 4)
print('b: ', b)
c = torch.linalg.matmul(a, b)
print('c: ', c)