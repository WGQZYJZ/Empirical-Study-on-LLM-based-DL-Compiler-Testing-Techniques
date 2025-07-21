'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resize_\ntorch.Tensor.resize_(_input_tensor, *sizes, memory_format=torch.contiguous_format)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_tensor = torch.randint(0, 10, size=(2, 3, 4, 5), dtype=torch.int32)
print('Input tensor: ', input_tensor)
print('Task 3: Call the API torch.Tensor.resize_')
output_tensor = torch.Tensor.resize_(input_tensor, 2, 3, 4, 5)
print('Output tensor: ', output_tensor)