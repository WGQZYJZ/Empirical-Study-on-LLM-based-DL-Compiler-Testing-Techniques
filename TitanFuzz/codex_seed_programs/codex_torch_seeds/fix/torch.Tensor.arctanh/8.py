'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arctanh\ntorch.Tensor.arctanh(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.arctanh(input_tensor)
print('Input tensor: ', input_tensor)
print('Output tensor: ', output_tensor)