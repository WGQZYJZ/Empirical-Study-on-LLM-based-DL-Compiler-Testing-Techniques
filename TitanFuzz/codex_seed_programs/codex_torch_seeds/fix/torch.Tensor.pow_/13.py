'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pow_\ntorch.Tensor.pow_(_input_tensor, exponent)\n'
import torch
input_tensor = torch.rand(5, 5, requires_grad=True)
output_tensor = torch.Tensor.pow_(input_tensor, 2)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)