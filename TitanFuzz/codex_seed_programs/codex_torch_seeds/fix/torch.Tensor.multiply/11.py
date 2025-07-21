'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multiply\ntorch.Tensor.multiply(_input_tensor, value)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.multiply(input_tensor, 2)
print('Output tensor: ', output_tensor)