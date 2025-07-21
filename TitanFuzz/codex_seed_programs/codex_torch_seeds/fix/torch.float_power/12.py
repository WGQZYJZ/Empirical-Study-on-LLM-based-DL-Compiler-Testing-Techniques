'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.float_power\ntorch.float_power(input, exponent, *, out=None)\n'
import torch
input = torch.randn(2, 3)
print('Input: ', input)
exponent = torch.randn(2, 3)
print('Exponent: ', exponent)
output = torch.float_power(input, exponent)
print('Output: ', output)