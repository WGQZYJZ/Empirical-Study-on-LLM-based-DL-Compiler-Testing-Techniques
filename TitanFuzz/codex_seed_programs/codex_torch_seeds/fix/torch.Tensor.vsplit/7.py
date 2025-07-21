'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.vsplit\ntorch.Tensor.vsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print('Input tensor: \n', input_tensor)
split_size_or_sections = 2
output_tensor = torch.Tensor.vsplit(input_tensor, split_size_or_sections)
print('Output tensor: \n', output_tensor)