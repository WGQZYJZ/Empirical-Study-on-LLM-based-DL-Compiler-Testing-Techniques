'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.divide\ntorch.Tensor.divide(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.randn(4, 4)
output_tensor = input_tensor.divide(2)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)