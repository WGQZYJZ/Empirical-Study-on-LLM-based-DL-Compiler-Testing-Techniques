'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.float_power\ntorch.float_power(input, exponent, *, out=None)\n'
import torch
input_data = torch.randn(1, 3)
print('Input data is: ', input_data)
exponent = torch.tensor([2.0])
print('Exponent is: ', exponent)
output = torch.float_power(input_data, exponent)
print('Output is: ', output)