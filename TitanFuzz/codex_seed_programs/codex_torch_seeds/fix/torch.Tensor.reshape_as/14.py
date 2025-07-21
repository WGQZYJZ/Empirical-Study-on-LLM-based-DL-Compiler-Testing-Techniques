'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reshape_as\ntorch.Tensor.reshape_as(_input_tensor, other)\n'
import torch
_input_tensor = torch.randn(2, 3)
_other_tensor = torch.randn(3, 2)
_output_tensor = _input_tensor.reshape_as(_other_tensor)
print('Input Tensor: {}'.format(_input_tensor))
print('Other Tensor: {}'.format(_other_tensor))
print('Output Tensor: {}'.format(_output_tensor))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reshape\ntorch.Tensor.reshape(_input_tensor, shape)\n'
import torch
_input_tensor = torch.randn(2, 3)
_output_tensor = _input_tensor.reshape(3, 2)
print('Input Tensor: {}'.format(_input_tensor))
print('Output Tensor: {}'.format(_output_tensor))