'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frexp\ntorch.frexp(input, *, out=None)\n'
import torch
data = torch.rand(5, 3)
print('Input data: ', data)
(mantissa, exponent) = torch.frexp(data)
print('Mantissa: ', mantissa)
print('Exponent: ', exponent)