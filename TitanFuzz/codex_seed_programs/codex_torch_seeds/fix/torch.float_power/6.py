'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.float_power\ntorch.float_power(input, exponent, *, out=None)\n'
import torch
input = torch.rand(4, 4)
exponent = torch.rand(4, 4)
out = torch.float_power(input, exponent)
print(out)