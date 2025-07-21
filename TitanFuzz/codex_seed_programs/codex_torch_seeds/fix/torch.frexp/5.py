'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frexp\ntorch.frexp(input, *, out=None)\n'
import torch
x = torch.randn(4)
print('Input data: ', x)
(significand, exponent) = torch.frexp(x)
print('Significand: ', significand)
print('Exponent: ', exponent)