'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.float_power\ntorch.float_power(input, exponent, *, out=None)\n'
import torch
input = torch.randn(2, 3)
exponent = torch.randn(2, 3)
print(torch.float_power(input, exponent))