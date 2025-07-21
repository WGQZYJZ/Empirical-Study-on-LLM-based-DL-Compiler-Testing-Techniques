'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor_divide\ntorch.Tensor.floor_divide(_input_tensor, value)\n'
import torch
input_tensor = torch.rand(4, 4)
print('input_tensor: ', input_tensor)
output_tensor = input_tensor.floor_divide(2)
print('output_tensor: ', output_tensor)