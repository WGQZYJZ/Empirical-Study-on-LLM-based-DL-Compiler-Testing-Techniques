'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sgn\ntorch.sgn(input, *, out=None)\n'
import torch
a = torch.randn(4, 4)
print('Input data:\n', a)
b = torch.sgn(a)
print('Output data:\n', b)