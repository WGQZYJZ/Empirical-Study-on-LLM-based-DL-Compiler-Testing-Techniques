'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arctanh\ntorch.arctanh(input, *, out=None)\n'
import torch
x = torch.randn(1, 2, 3, requires_grad=True)
y = torch.arctanh(x)
print('The input data: ', x)
print('The result of arctanh: ', y)