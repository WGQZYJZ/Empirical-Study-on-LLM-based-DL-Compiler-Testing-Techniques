'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atan2\ntorch.atan2(input, other, *, out=None)\n'
import torch
x = torch.randn(4)
y = torch.randn(4)
print('Input x: ', x)
print('Input y: ', y)
print('Output: ', torch.atan2(x, y))