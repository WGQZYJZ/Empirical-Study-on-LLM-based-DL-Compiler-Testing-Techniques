'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.signbit\ntorch.signbit(input, *, out=None)\n'
import torch
x = torch.randn(1, 3)
print('x: {}'.format(x))
print('torch.signbit(x): {}'.format(torch.signbit(x)))