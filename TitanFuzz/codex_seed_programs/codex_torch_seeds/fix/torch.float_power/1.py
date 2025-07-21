'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.float_power\ntorch.float_power(input, exponent, *, out=None)\n'
import torch
import torch
input = torch.rand(3, 3)
print('input: ', input)
out = torch.float_power(input, 3)
print('out: ', out)