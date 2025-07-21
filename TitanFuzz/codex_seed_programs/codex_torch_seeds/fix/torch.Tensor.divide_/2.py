'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.divide_\ntorch.Tensor.divide_(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input_tensor: ', input_tensor)
output_tensor = torch.Tensor.divide_(input_tensor, 2)
print('Output_tensor: ', output_tensor)