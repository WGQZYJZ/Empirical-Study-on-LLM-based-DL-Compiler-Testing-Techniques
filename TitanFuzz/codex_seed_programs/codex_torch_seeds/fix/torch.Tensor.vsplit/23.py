'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.vsplit\ntorch.Tensor.vsplit(_input_tensor, split_size_or_sections)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_tensor = torch.randn(2, 3, 4)
print('input_tensor: {}'.format(input_tensor))
print('Task 3: Call the API torch.Tensor.vsplit')
output_tensor_list = torch.Tensor.vsplit(input_tensor, 2)
print('output_tensor_list: {}'.format(output_tensor_list))