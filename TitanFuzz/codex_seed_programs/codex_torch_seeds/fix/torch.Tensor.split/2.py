'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.split\ntorch.Tensor.split(_input_tensor, split_size, dim=0)\n'
import torch
input_tensor = torch.randn(size=(10, 5))
split_size = 3
dim = 0
output_tensor = torch.split(input_tensor, split_size, dim)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)