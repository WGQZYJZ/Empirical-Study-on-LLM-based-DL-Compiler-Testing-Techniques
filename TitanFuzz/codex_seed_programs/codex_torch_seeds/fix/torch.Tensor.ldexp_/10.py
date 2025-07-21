'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ldexp_\ntorch.Tensor.ldexp_(_input_tensor, other)\n'
import torch
import torch
input_tensor = torch.randn(4, 4)
other = torch.randn(4, 4)
output_tensor = torch.Tensor.ldexp_(input_tensor, other)
print('input_tensor:', input_tensor)
print('other:', other)
print('output_tensor:', output_tensor)