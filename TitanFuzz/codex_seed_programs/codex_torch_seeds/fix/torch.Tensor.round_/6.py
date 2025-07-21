'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.round_\ntorch.Tensor.round_(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 3)
_output_tensor = torch.Tensor.round_(_input_tensor)
print('\nTask 3: Call the API torch.Tensor.round_')
print('Input: {}'.format(_input_tensor))
print('Output: {}'.format(_output_tensor))
'\nTask 4: Call the API torch.round_\ntorch.round_(_input_tensor)\n'
_output_tensor = torch.round_(_input_tensor)
print('\nTask 4: Call the API torch.round_')
print('Input: {}'.format(_input_tensor))
print('Output: {}'.format(_output_tensor))