'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.asinh_\ntorch.Tensor.asinh_(_input_tensor)\n'
import torch
input_tensor = torch.rand(1, 3, 3)
print('Input tensor is: \n', input_tensor)
output_tensor = torch.Tensor.asinh_(input_tensor)
print('Output tensor is: \n', output_tensor)