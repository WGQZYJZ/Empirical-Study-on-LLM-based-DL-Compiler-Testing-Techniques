'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arcsinh\ntorch.arcsinh(input, *, out=None)\n'
import torch
x = torch.randn(4, 4)
print('x: \n', x)
y = torch.arcsinh(x)
print('y: \n', y)