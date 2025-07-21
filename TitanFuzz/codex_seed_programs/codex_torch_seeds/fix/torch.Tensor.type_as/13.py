'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type_as\ntorch.Tensor.type_as(_input_tensor, tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
print('Input tensor:', input_tensor)
output_tensor = torch.Tensor.type_as(input_tensor, torch.IntTensor())
print('Output tensor:', output_tensor)