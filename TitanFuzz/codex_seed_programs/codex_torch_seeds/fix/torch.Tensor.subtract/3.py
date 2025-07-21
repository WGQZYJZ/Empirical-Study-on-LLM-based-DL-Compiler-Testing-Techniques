'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract\ntorch.Tensor.subtract(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.randn(5, 3)
other = torch.randn(5, 3)
print('Input Tensor:', input_tensor)
print('Other:', other)
output_tensor = torch.Tensor.subtract(input_tensor, other)
print('Output Tensor:', output_tensor)