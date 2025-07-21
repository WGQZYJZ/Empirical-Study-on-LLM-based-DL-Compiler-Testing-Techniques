'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isclose\ntorch.Tensor.isclose(_input_tensor, other, rtol=1e-05, atol=1e-08, equal_nan=False)\n'
import torch
input_tensor = torch.rand(3, 3)
other = torch.rand(3, 3)
output_tensor = input_tensor.isclose(other)
print('input_tensor: ', input_tensor)
print('other: ', other)
print('output_tensor: ', output_tensor)