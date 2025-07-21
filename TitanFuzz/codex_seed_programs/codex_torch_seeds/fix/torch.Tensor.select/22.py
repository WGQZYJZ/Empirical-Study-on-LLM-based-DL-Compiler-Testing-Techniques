'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.select\ntorch.Tensor.select(_input_tensor, dim, index)\n'
import torch
input_tensor = torch.rand(4, 3, 28, 28)
output_tensor = torch.Tensor.select(input_tensor, 1, 2)
print('The input tensor is: ', input_tensor)
print('The output tensor is: ', output_tensor)