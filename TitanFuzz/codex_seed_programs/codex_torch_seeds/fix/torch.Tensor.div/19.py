'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.div\ntorch.Tensor.div(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input Tensor: ', input_tensor)
output_tensor = input_tensor.div(2)
print('Output Tensor: ', output_tensor)