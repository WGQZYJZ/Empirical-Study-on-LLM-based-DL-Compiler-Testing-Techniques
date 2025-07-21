'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.float_power_\ntorch.Tensor.float_power_(_input_tensor, exponent)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input Tensor: ', input_tensor)
output_tensor = input_tensor.float_power_(2)
print('Output Tensor: ', output_tensor)