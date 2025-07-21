'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resize_as_\ntorch.Tensor.resize_as_(_input_tensor, tensor, memory_format=torch.contiguous_format)\n'
import torch
input_tensor = torch.randn(2, 3, 5, 5)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor()
torch.Tensor.resize_as_(output_tensor, input_tensor, memory_format=torch.contiguous_format)
print('Output tensor: ', output_tensor)