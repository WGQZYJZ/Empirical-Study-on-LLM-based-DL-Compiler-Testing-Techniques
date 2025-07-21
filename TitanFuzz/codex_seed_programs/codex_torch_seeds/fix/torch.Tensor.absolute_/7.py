'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.absolute_\ntorch.Tensor.absolute_(_input_tensor)\n'
import torch
_input_tensor = torch.randn(5, 3)
_absolute_tensor = torch.Tensor.absolute_(_input_tensor)
print('Input Tensor: ', _input_tensor)
print('Absolute Tensor: ', _absolute_tensor)