'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ge\ntorch.ge(input, other, *, out=None)\n'
import torch
x = torch.randn(1)
y = torch.randn(1)
print('x: ', x)
print('y: ', y)
print('x>=y: ', torch.ge(x, y))
print('x>=y: ', torch.ge(x, x))