'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arcsinh\ntorch.arcsinh(input, *, out=None)\n'
import torch
x = torch.randn(4, 4)
print('Input tensor: ', x)
y = torch.arcsinh(x)
print('Output tensor: ', y)