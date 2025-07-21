'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pow_\ntorch.Tensor.pow_(_input_tensor, exponent)\n'
import torch
input_tensor = torch.randn(3, 4)
print('Input tensor: ', input_tensor)
exponent = 2
output_tensor = input_tensor.pow_(exponent)
print('Output tensor: ', output_tensor)