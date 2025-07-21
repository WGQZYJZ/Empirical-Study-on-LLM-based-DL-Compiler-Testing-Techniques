'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.negative_\ntorch.Tensor.negative_(_input_tensor)\n'
import torch
'\nTask 1: import PyTorch\n'
'\nTask 2: Generate input data\n'
input_tensor = torch.rand(3, 3)
print('input_tensor:', input_tensor)
'\nTask 3: Call the API torch.Tensor.negative_\ntorch.Tensor.negative_(_input_tensor)\n'
output_tensor = torch.Tensor.negative_(input_tensor)
print('output_tensor:', output_tensor)