'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multiply\ntorch.Tensor.multiply(_input_tensor, value)\n'
import torch
input_tensor = torch.rand(2, 3)
output_tensor = torch.Tensor.multiply(input_tensor, 2)
print('input tensor: ', input_tensor)
print('output tensor: ', output_tensor)