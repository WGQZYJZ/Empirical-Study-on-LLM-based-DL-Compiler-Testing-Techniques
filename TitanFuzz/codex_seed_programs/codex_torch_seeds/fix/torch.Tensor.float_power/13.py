'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.float_power\ntorch.Tensor.float_power(_input_tensor, exponent)\n'
import torch
input_tensor = torch.rand(3, 3)
print('Input data:')
print(input_tensor)
exponent = 2
output_tensor = torch.Tensor.float_power(input_tensor, exponent)
print('Output data:')
print(output_tensor)