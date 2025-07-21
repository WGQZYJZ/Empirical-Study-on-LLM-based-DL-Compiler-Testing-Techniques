'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type_as\ntorch.Tensor.type_as(_input_tensor, tensor)\n'
import torch
import torch
input_tensor = torch.rand(4, 2)
print('input_tensor: ', input_tensor)
output_tensor = input_tensor.type_as(torch.ones(2, 2))
print('output_tensor: ', output_tensor)