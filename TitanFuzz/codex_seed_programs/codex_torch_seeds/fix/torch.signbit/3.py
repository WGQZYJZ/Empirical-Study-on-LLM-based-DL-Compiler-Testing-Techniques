'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.signbit\ntorch.signbit(input, *, out=None)\n'
import torch
x = torch.randn(3, 3)
print('Input data: ', x)
print('Sign bit of input: ', torch.signbit(x))