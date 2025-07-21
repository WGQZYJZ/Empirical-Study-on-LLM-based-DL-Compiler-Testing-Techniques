'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ldexp_\ntorch.Tensor.ldexp_(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(4, 4)
other = torch.randn(4, 4)
print('Input tensor: ', input_tensor)
print('Input other: ', other)
print('Output tensor: ', torch.Tensor.ldexp_(input_tensor, other))
print('Input tensor: ', input_tensor)