'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type_as\ntorch.Tensor.type_as(_input_tensor, tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.type_as(input_tensor, torch.FloatTensor())
print('The input tensor is:', input_tensor)
print('The output tensor is:', output_tensor)