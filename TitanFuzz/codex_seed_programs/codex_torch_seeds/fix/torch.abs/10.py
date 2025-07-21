'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.abs\ntorch.abs(input, *, out=None)\n'
import torch
x = torch.randn(1, 3, requires_grad=True)
print('x:', x)
y = torch.abs(x)
print('y:', y)