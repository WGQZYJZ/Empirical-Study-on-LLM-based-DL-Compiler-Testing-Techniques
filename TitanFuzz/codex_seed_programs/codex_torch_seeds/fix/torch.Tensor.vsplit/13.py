'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.vsplit\ntorch.Tensor.vsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print(input_tensor)
print('\nTask 2: Generate input data')
print('input_tensor.shape:', input_tensor.shape)
print('input_tensor.size():', input_tensor.size())
print('input_tensor.dim():', input_tensor.dim())
print('\nTask 3: Call the API torch.Tensor.vsplit')
output_tensor_list = torch.Tensor.vsplit(input_tensor, 2)
for i in range(len(output_tensor_list)):
    print('output_tensor_list[{}]:'.format(i), output_tensor_list[i])
print('\noutput_tensor_list[0]:', output_tensor_list[0])