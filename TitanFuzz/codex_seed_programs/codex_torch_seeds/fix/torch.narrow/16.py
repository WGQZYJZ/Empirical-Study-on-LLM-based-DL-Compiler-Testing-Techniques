'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.narrow\ntorch.narrow(input, dim, start, length)\n'
import torch
a = torch.randn(4, 4)
print('a: \n', a)
b = torch.narrow(a, 0, 1, 3)
print('b: \n', b)
c = torch.narrow(a, 1, 1, 3)
print('c: \n', c)