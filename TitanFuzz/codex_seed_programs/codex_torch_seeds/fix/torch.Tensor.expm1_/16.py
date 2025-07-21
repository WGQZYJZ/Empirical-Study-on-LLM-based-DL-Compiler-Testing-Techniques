'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expm1_\ntorch.Tensor.expm1_(_input_tensor)\n'
import torch
input_tensor = torch.randn(5, 5)
print('Input tensor:', input_tensor)
output_tensor = torch.Tensor.expm1_(input_tensor)
print('Output tensor:', output_tensor)