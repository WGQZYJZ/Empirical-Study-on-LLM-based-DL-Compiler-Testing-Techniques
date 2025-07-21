'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frexp\ntorch.frexp(input, *, out=None)\n'
import torch
import torch
x = torch.randn(4)
print('Input data: ', x)
(mantissa, exponent) = torch.frexp(x)
print('Mantissa: ', mantissa)
print('Exponent: ', exponent)