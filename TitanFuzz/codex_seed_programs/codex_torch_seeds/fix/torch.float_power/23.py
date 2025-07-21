'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.float_power\ntorch.float_power(input, exponent, *, out=None)\n'
import torch
input = torch.randn(3, 3, 3)
print('input = ', input)
exponent = torch.tensor([1, 2, 3])
print('exponent = ', exponent)
output = torch.float_power(input, exponent)
print('output = ', output)