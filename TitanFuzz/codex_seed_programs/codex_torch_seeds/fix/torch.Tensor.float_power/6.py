'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.float_power\ntorch.Tensor.float_power(_input_tensor, exponent)\n'
import torch
input_tensor = torch.rand(2, 2)
exponent = torch.rand(1)
print('Input tensor:')
print(input_tensor)
print('Exponent:')
print(exponent)
output_tensor = torch.Tensor.float_power(input_tensor, exponent)
print('Output tensor:')
print(output_tensor)