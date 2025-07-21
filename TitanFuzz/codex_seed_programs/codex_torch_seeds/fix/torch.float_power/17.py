'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.float_power\ntorch.float_power(input, exponent, *, out=None)\n'
import torch
input = torch.randn(5, 3, dtype=torch.float)
exponent = torch.randn(5, 3, dtype=torch.float)
output = torch.float_power(input, exponent)
print('Input: ', input)
print('Exponent: ', exponent)
print('Output: ', output)