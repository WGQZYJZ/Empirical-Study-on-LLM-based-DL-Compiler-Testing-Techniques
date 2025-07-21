'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pow_\ntorch.Tensor.pow_(_input_tensor, exponent)\n'
import torch
input_tensor = torch.arange(0, 5)
exponent = 2
result = torch.Tensor.pow_(input_tensor, exponent)
print('The input tensor is: {}'.format(input_tensor))
print('The result tensor is: {}'.format(result))