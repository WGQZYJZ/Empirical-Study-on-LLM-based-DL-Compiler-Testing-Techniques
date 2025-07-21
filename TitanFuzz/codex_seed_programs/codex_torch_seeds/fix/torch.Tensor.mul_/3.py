'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mul_\ntorch.Tensor.mul_(_input_tensor, value)\n'
import torch
input_tensor = torch.randn(1, 3)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.mul_(input_tensor, 10)
print('Output tensor: ', output_tensor)