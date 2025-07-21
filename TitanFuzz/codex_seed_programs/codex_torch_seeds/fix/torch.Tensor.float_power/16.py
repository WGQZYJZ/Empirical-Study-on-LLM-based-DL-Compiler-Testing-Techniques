'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.float_power\ntorch.Tensor.float_power(_input_tensor, exponent)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input tensor: \n', input_tensor)
exponent = torch.randn(1, 1)
print('exponent: \n', exponent)
output_tensor = input_tensor.float_power(exponent)
print('Output tensor: \n', output_tensor)