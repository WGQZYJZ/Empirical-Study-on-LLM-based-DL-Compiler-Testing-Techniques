'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.divide_\ntorch.Tensor.divide_(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input Tensor: ', input_tensor)
output_tensor = torch.Tensor.divide_(input_tensor, 2)
print('Output Tensor: ', output_tensor)