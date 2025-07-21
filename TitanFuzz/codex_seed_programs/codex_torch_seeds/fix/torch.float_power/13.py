'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.float_power\ntorch.float_power(input, exponent, *, out=None)\n'
import torch
input_data = torch.randn(1, 3)
print('input_data: ', input_data)
output = torch.float_power(input_data, 3)
print('output: ', output)