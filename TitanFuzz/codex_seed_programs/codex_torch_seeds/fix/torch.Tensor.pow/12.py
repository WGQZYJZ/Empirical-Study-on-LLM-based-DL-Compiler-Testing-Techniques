'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pow\ntorch.Tensor.pow(_input_tensor, exponent)\n'
import torch
input_tensor = torch.rand(2, 3)
exponent = 2
output_tensor = input_tensor.pow(exponent)
print('The input tensor is:', input_tensor)
print('The exponent is:', exponent)
print('The output tensor is:', output_tensor)