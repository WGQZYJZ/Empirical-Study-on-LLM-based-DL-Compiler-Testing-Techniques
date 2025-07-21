'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.float_power\ntorch.Tensor.float_power(_input_tensor, exponent)\n'
import torch
input_tensor = torch.rand(10, 10)
print('Input Tensor:\n', input_tensor)
output_tensor = torch.Tensor.float_power(input_tensor, 2)
print('Output Tensor:\n', output_tensor)