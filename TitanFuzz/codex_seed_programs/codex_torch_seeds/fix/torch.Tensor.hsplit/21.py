'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hsplit\ntorch.Tensor.hsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9], [11, 12, 13, 14, 15, 16, 17, 18, 19], [21, 22, 23, 24, 25, 26, 27, 28, 29], [31, 32, 33, 34, 35, 36, 37, 38, 39]])
split_size_or_sections = 3
output_tensor = torch.Tensor.hsplit(input_tensor, split_size_or_sections)
print('input_tensor = ', input_tensor)
print('output_tensor = ', output_tensor)