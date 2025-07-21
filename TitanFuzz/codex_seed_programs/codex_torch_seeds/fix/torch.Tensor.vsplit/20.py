'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.vsplit\ntorch.Tensor.vsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.vsplit(input_tensor, 2)
print('Output tensor: ', output_tensor)
output_tensor = torch.Tensor.vsplit(input_tensor, [2, 3])
print('Output tensor: ', output_tensor)