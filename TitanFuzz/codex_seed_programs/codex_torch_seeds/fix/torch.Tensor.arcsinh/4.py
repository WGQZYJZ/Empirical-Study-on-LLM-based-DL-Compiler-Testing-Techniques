'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arcsinh\ntorch.Tensor.arcsinh(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
print('Input tensor: \n', input_tensor)
output_tensor = torch.Tensor.arcsinh(input_tensor)
print('Output tensor: \n', output_tensor)