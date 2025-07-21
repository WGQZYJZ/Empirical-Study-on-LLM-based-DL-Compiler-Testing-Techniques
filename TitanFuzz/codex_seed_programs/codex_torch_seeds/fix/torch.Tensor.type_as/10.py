'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type_as\ntorch.Tensor.type_as(_input_tensor, tensor)\n'
import torch
input_tensor = torch.rand(1, 3, 224, 224)
output_tensor = torch.Tensor.type_as(input_tensor, torch.float16)
print('input tensor:', input_tensor)
print('output tensor:', output_tensor)