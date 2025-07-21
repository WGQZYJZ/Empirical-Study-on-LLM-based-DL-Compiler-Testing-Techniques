'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.div\ntorch.Tensor.div(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.randn(2, 3)
print('input_tensor: ', input_tensor)
output_tensor = input_tensor.div(2.0)
print('output_tensor: ', output_tensor)