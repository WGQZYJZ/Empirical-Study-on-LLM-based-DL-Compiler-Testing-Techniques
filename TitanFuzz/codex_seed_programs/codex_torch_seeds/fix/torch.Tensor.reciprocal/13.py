'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reciprocal\ntorch.Tensor.reciprocal(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 3, dtype=torch.float32)
_output_tensor = torch.Tensor.reciprocal(_input_tensor)
print('Input: {}'.format(_input_tensor))
print('Output: {}'.format(_output_tensor))
_output_tensor = torch.reciprocal(_input_tensor)
print('Output: {}'.format(_output_tensor))
_input_tensor.reciprocal_()
print('Input: {}'.format(_input_tensor))