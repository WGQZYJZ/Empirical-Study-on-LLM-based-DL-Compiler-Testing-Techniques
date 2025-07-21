'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mul\ntorch.Tensor.mul(_input_tensor, value)\n'
import torch
_input_tensor = torch.rand(4, 3)
print('Input tensor: {}'.format(_input_tensor))
_output_tensor = _input_tensor.mul(2)
print('Output tensor: {}'.format(_output_tensor))