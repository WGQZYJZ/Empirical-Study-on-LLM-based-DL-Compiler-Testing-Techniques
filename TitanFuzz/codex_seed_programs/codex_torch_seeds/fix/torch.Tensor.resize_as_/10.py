'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resize_as_\ntorch.Tensor.resize_as_(_input_tensor, tensor, memory_format=torch.contiguous_format)\n'
import torch
input_tensor = torch.rand(2, 3, 4, 5)
print('Input tensor: ', input_tensor)
resize_tensor = torch.rand(2, 3, 4, 5)
print('Resize tensor: ', resize_tensor)
resize_tensor.resize_as_(input_tensor)
print('Resize tensor after resize_as_: ', resize_tensor)