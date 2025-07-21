'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arcsinh\ntorch.Tensor.arcsinh(_input_tensor)\n'
import torch
input_tensor = torch.rand(3, 3)
output_tensor = input_tensor.arcsinh()
print('Input tensor: ', input_tensor)
print('Output tensor: ', output_tensor)