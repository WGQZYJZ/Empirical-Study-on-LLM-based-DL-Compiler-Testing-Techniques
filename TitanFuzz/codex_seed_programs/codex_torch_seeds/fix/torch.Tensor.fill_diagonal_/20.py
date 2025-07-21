'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fill_diagonal_\ntorch.Tensor.fill_diagonal_(_input_tensor, fill_value, wrap=False)\n'
import torch
_input_tensor = torch.randn(3, 3)
print('Input Tensor: {}'.format(_input_tensor))
_input_tensor.fill_diagonal_(0)
print('Output Tensor: {}'.format(_input_tensor))