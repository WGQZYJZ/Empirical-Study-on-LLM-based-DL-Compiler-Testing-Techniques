'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hsplit\ntorch.Tensor.hsplit(_input_tensor, split_size_or_sections)\n'
import torch
import torch
input_tensor = torch.arange(0, 12)
input_tensor = input_tensor.view(3, 4)
print('Input tensor is: ', input_tensor)
split_tensor = input_tensor.hsplit(2)
print('Split tensor is: ', split_tensor)
split_tensor = input_tensor.hsplit(4)
print('Split tensor is: ', split_tensor)