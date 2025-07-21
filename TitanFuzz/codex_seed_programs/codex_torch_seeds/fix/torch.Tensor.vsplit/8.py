'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.vsplit\ntorch.Tensor.vsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.arange(0, 16, 1)
input_tensor = input_tensor.view(4, 4)
print('The input tensor is:')
print(input_tensor)
split_tensor = torch.Tensor.vsplit(input_tensor, 2)
print('The split tensor is:')
print(split_tensor)