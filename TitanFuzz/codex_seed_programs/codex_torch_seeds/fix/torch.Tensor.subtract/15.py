'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract\ntorch.Tensor.subtract(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.randn(5, 3)
output_tensor = input_tensor.subtract(5)
print('Input tensor:', input_tensor)
print('Output tensor:', output_tensor)