'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor\ntorch.floor(input, *, out=None)\n'
import torch
x = torch.randn(1)
print('x:', x)
y = torch.floor(x)
print('y:', y)