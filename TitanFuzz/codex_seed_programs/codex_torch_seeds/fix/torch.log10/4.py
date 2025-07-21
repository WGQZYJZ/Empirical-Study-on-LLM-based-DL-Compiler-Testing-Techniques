'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log10\ntorch.log10(input, *, out=None)\n'
import torch
x = torch.randn(4, 4)
print('x =', x)
y = torch.log10(x)
print('y =', y)