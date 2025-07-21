'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.float_power_\ntorch.Tensor.float_power_(_input_tensor, exponent)\n'
import torch
input_tensor = torch.rand(2, 3)
print('input_tensor: ', input_tensor)
exponent = torch.tensor(2.0)
output_tensor = torch.Tensor.float_power_(input_tensor, exponent)
print('output_tensor: ', output_tensor)