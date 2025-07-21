'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tanh\ntorch.tanh(input, *, out=None)\n'
import torch
x = torch.randn(1, 3)
print('x: ', x)
y = torch.tanh(x)
print('y: ', y)