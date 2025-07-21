'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.inner\ntorch.Tensor.inner(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(2, 3)
other = torch.randn(3, 2)
output = torch.Tensor.inner(input_tensor, other)
print('input_tensor:', input_tensor)
print('other:', other)
print('output:', output)