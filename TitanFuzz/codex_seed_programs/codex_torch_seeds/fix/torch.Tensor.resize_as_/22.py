'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resize_as_\ntorch.Tensor.resize_as_(_input_tensor, tensor, memory_format=torch.contiguous_format)\n'
import torch
input_tensor = torch.randn(2, 3, 4, 5)
print('input_tensor: ', input_tensor.shape)
output_tensor = torch.randn(2, 3, 4, 5)
input_tensor.resize_as_(output_tensor)
print('output_tensor: ', output_tensor.shape)