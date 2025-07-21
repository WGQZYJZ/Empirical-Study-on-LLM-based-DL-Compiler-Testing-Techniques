'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type_as\ntorch.Tensor.type_as(_input_tensor, tensor)\n'
import torch
input_tensor = torch.rand(1, 1, 2, 2)
print(input_tensor)
print(input_tensor.type_as(torch.ones(1, 1, 2, 2)))