'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.split\ntorch.Tensor.split(_input_tensor, split_size, dim=0)\n'
import torch
_input_tensor = torch.randn(3, 4, 5)
_split_size = 3
_dim = 1
print('Input Tensor: \n', _input_tensor)
_output_tensor = _input_tensor.split(_split_size, dim=_dim)
print('Output Tensor: \n', _output_tensor)