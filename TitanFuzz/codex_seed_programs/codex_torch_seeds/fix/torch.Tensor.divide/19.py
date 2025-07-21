'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.divide\ntorch.Tensor.divide(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.rand(10, requires_grad=True)
print('input_tensor:', input_tensor)
output_tensor = input_tensor.divide(10)
print('output_tensor:', output_tensor)