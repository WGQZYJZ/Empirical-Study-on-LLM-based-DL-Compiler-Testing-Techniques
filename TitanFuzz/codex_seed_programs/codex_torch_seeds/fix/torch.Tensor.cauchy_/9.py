'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cauchy_\ntorch.Tensor.cauchy_(_input_tensor, median=0, sigma=1, *, generator=None)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input Tensor: ', input_tensor)
output_tensor = torch.Tensor.cauchy_(input_tensor)
print('Output Tensor: ', output_tensor)