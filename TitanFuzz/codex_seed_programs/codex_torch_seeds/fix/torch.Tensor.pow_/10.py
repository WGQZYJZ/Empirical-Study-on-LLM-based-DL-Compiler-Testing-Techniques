'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pow_\ntorch.Tensor.pow_(_input_tensor, exponent)\n'
import torch
input_tensor = torch.randn(2, 3, 4, 5)
exponent = 2
output_tensor = input_tensor.pow_(exponent)
print('input_tensor: {}'.format(input_tensor))
print('output_tensor: {}'.format(output_tensor))