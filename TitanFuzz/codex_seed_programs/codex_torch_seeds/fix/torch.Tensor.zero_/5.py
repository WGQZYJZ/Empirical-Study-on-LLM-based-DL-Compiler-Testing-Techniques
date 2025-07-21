'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.zero_\ntorch.Tensor.zero_(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 3)
print('Input tensor:')
print(_input_tensor)
_zero_tensor = torch.Tensor.zero_(_input_tensor)
print('Zero tensor:')
print(_zero_tensor)