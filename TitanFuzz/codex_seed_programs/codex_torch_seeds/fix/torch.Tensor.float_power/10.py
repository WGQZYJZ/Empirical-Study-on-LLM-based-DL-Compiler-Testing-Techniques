'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.float_power\ntorch.Tensor.float_power(_input_tensor, exponent)\n'
import torch
input_tensor = torch.rand(3, 4)
print('Input tensor:', input_tensor)
output_tensor = input_tensor.float_power(2)
print('Output tensor:', output_tensor)