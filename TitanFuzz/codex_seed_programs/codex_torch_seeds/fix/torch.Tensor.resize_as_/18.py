'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resize_as_\ntorch.Tensor.resize_as_(_input_tensor, tensor, memory_format=torch.contiguous_format)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input Tensor: ', input_tensor)
resize_as_tensor = torch.randn(2, 3)
print('Resize As Tensor: ', resize_as_tensor)
torch.Tensor.resize_as_(input_tensor, resize_as_tensor)
print('Resized Input Tensor: ', input_tensor)