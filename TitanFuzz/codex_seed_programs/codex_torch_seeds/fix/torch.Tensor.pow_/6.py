'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pow_\ntorch.Tensor.pow_(_input_tensor, exponent)\n'
import torch
input_tensor = torch.arange(1, 11)
exponent = 2
output_tensor = input_tensor.pow_(exponent)
print('Output Tensor: ', output_tensor)
'\nTask 4: Call the API torch.Tensor.pow\ntorch.Tensor.pow(_input_tensor, exponent)\n'
output_tensor = input_tensor.pow(exponent)
print('Output Tensor: ', output_tensor)