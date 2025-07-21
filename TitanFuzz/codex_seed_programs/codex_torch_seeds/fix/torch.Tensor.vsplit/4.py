'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.vsplit\ntorch.Tensor.vsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.arange(0, 12)
input_tensor = input_tensor.view(3, 4)
print('Input tensor:\n{}'.format(input_tensor))
output_tensor_list = torch.Tensor.vsplit(input_tensor, 2)
print('Output tensor list:\n{}'.format(output_tensor_list))