'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hsplit\ntorch.Tensor.hsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print('Input Tensor: ', input_tensor)
split_tensor = torch.Tensor.hsplit(input_tensor, 2)
print('Split Tensor: ', split_tensor)
split_tensor = torch.Tensor.hsplit(input_tensor, [1, 3])
print('Split Tensor: ', split_tensor)