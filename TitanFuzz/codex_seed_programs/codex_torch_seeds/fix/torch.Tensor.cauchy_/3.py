'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cauchy_\ntorch.Tensor.cauchy_(_input_tensor, median=0, sigma=1, *, generator=None)\n'
import torch
input_tensor = torch.rand(10)
print('Input tensor:', input_tensor)
output_tensor = torch.Tensor.cauchy_(input_tensor, median=1, sigma=2)
print('Output tensor:', output_tensor)