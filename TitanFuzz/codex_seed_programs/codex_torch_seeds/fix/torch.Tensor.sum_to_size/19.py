'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sum_to_size\ntorch.Tensor.sum_to_size(_input_tensor, *size)\n'
import torch
import torch
input_tensor = torch.rand(3, 2, 5)
output_tensor = input_tensor.sum_to_size(3, 5)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)