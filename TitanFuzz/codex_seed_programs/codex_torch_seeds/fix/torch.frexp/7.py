'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frexp\ntorch.frexp(input, *, out=None)\n'
import torch
x = torch.randn(4)
print('x = ', x)
(mantissa, exponent) = torch.frexp(x)
print('mantissa = ', mantissa)
print('exponent = ', exponent)