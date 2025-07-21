'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resize_as_\ntorch.Tensor.resize_as_(_input_tensor, tensor, memory_format=torch.contiguous_format)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print('input_tensor: ', input_tensor)
tensor = torch.randn(3, 4)
print('tensor: ', tensor)
input_tensor.resize_as_(tensor)
print('input_tensor: ', input_tensor)