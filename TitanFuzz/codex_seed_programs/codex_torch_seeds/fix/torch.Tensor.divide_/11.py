'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.divide_\ntorch.Tensor.divide_(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.rand(10)
print('input_tensor: ', input_tensor)
print('torch.Tensor.divide_(input_tensor, 2): ', torch.Tensor.divide_(input_tensor, 2))
print('input_tensor: ', input_tensor)