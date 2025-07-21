'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type_as\ntorch.Tensor.type_as(_input_tensor, tensor)\n'
import torch
input_tensor = torch.rand(2, 3, 4)
output_tensor = input_tensor.type_as(torch.IntTensor())
print('input_tensor = ', input_tensor)
print('output_tensor = ', output_tensor)