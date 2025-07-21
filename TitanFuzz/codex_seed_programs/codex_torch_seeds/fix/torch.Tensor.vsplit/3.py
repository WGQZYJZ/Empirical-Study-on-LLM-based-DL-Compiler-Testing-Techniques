'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.vsplit\ntorch.Tensor.vsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.rand(2, 3, 4)
print('Input tensor: ', input_tensor)
split_tensor = input_tensor.vsplit(2)
print('Split tensor: ', split_tensor)