'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type_as\ntorch.Tensor.type_as(_input_tensor, tensor)\n'
import torch
import numpy as np
print('Task 1: import PyTorch')
print('\nTask 2: Generate input data')
_input_tensor = torch.randn(3, 4, 5)
print('\n_input_tensor = {}'.format(_input_tensor))
print('\nTask 3: Call the API torch.Tensor.type_as')
_tensor = torch.randn(3, 4, 5)
print('\n_tensor = {}'.format(_tensor))
_output_tensor = _input_tensor.type_as(_tensor)
print('\n_output_tensor = {}'.format(_output_tensor))