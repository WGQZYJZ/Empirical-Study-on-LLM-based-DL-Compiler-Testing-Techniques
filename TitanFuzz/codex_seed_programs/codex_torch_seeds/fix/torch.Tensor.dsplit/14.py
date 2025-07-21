'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dsplit\ntorch.Tensor.dsplit(_input_tensor, split_size_or_sections)\n'
import torch
import torch
input_tensor = torch.arange(1, 10).view(3, 3)
print('input_tensor = ', input_tensor)
output_tensor_list = torch.Tensor.dsplit(input_tensor, 2)
print('output_tensor_list = ', output_tensor_list)
output_tensor_list = torch.Tensor.dsplit(input_tensor, [2, 4])
print('output_tensor_list = ', output_tensor_list)