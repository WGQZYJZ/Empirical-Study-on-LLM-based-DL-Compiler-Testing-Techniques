'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_and\ntorch.Tensor.logical_and(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(5, 5)
other = torch.rand(5, 5)
output_tensor = input_tensor.logical_and(other)
print('input_tensor:', input_tensor)
print('other:', other)
print('output_tensor:', output_tensor)