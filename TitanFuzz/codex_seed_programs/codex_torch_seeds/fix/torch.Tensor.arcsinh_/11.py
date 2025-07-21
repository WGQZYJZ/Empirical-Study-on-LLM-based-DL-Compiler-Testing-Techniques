'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arcsinh_\ntorch.Tensor.arcsinh_(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print('input_tensor:', input_tensor)
output_tensor = torch.Tensor.arcsinh_(input_tensor)
print('output_tensor:', output_tensor)