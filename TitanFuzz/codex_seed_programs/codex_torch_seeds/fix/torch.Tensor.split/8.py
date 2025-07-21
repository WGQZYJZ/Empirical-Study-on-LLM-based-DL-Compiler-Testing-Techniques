'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.split\ntorch.Tensor.split(_input_tensor, split_size, dim=0)\n'
import torch
print('Import PyTorch successfully.')
_input_tensor = torch.randn(3, 4)
print('Input tensor: \n', _input_tensor)
_output_tensor = _input_tensor.split(split_size=2, dim=1)
print('Output tensor: \n', _output_tensor)
_output_tensor = _input_tensor.split(split_size=[2, 1], dim=1)
print('Output tensor: \n', _output_tensor)
_output_tensor = _input_tensor.split(split_size=[2, 1], dim=0)
print('Output tensor: \n', _output_tensor)