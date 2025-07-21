'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.float_power\ntorch.float_power(input, exponent, *, out=None)\n'
import torch
input = torch.randn(5, 5)
print('Input data: \n', input)
exponent = torch.randn(5, 5)
print('Exponent: \n', exponent)
output = torch.float_power(input, exponent)
print('Output data: \n', output)