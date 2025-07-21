'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.div\ntorch.Tensor.div(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.rand(4, 4)
value = 0.5
output_tensor = input_tensor.div(value)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)