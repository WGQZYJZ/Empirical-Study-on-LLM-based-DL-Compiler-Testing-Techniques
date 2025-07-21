'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pow\ntorch.Tensor.pow(_input_tensor, exponent)\n'
import torch
input_tensor = torch.randn(4, 4)
output_tensor = input_tensor.pow(3)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)