'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.float_power\ntorch.float_power(input, exponent, *, out=None)\n'
import torch
a = torch.arange(9, dtype=torch.float)
print('Input: ', a)
b = torch.float_power(a, 2)
print('Output: ', b)