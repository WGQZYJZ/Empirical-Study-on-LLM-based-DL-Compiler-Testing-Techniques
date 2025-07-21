'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resize_as_\ntorch.Tensor.resize_as_(_input_tensor, tensor, memory_format=torch.contiguous_format)\n'
import torch
input_tensor = torch.rand(4, 4)
tensor = torch.rand(2, 2)
output_tensor = torch.Tensor.resize_as_(input_tensor, tensor)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)