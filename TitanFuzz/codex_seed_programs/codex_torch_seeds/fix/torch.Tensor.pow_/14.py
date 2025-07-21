'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pow_\ntorch.Tensor.pow_(_input_tensor, exponent)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor: ', input_tensor)
exponent = 2
output_tensor = torch.Tensor.pow_(input_tensor, exponent)
print('Output tensor: ', output_tensor)