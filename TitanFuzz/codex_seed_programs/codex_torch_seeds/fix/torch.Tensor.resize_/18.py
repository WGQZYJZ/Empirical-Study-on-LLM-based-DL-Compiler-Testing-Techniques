'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resize_\ntorch.Tensor.resize_(_input_tensor, *sizes, memory_format=torch.contiguous_format)\n'
import torch
input_tensor = torch.rand(4, 4)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.resize_(input_tensor, 2, 2)
print('Output tensor: ', output_tensor)