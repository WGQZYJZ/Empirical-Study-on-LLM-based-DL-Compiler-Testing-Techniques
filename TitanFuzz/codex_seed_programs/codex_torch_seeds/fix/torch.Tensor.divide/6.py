'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.divide\ntorch.Tensor.divide(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor:', input_tensor)
divided_tensor = input_tensor.divide(2)
print('Divided tensor:', divided_tensor)