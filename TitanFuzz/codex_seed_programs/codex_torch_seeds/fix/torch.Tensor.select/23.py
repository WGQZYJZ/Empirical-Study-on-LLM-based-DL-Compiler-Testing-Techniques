'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.select\ntorch.Tensor.select(_input_tensor, dim, index)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print('Input tensor: \n', input_tensor)
dim = 0
index = 1
output_tensor = torch.Tensor.select(input_tensor, dim, index)
print('Output tensor: \n', output_tensor)