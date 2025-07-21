'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pow_\ntorch.Tensor.pow_(_input_tensor, exponent)\n'
import torch
input_tensor = torch.randn(5, 3)
exponent = 2
output_tensor = torch.Tensor.pow_(input_tensor, exponent)
print('Input Tensor:', input_tensor)
print('Output Tensor:', output_tensor)