'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reciprocal_\ntorch.Tensor.reciprocal_(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input Tensor:', input_tensor)
output_tensor = torch.Tensor.reciprocal_(input_tensor)
print('Output Tensor:', output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reciprocal\ntorch.Tensor.reciprocal(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input Tensor:', input_tensor)
output_tensor = torch.Tensor.reciprocal(input_tensor)
print('Output Tensor:', output_tensor)