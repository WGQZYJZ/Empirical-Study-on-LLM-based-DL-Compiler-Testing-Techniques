'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arctanh\ntorch.Tensor.arctanh(_input_tensor)\n'
import torch
input_tensor = torch.randn(10, 10)
print('Input data: ', input_tensor)
output_tensor = torch.Tensor.arctanh(input_tensor)
print('Output data: ', output_tensor)