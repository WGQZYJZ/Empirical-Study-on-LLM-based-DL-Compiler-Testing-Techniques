'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.float_power_\ntorch.Tensor.float_power_(_input_tensor, exponent)\n'
import torch
input_data = torch.arange(1, 11, dtype=torch.float32).reshape(1, 10)
print('Input tensor: ', input_data)
print('Output tensor: ', torch.Tensor.float_power_(input_data, 2))