'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resize_as_\ntorch.Tensor.resize_as_(_input_tensor, tensor, memory_format=torch.contiguous_format)\n'
import torch
input_tensor = torch.randint(0, 10, size=(2, 2))
print('input tensor: ', input_tensor)
output_tensor = torch.randint(0, 10, size=(3, 3))
print('output tensor: ', output_tensor)
output_tensor.resize_as_(input_tensor)
print('output tensor: ', output_tensor)