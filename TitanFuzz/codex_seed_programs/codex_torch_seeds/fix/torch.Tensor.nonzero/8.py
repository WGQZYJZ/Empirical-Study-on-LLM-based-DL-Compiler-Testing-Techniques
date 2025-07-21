'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nonzero\ntorch.Tensor.nonzero(_input_tensor, as_tuple=False)\n'
import torch
import torch
_input_tensor = torch.randn(3, 3)
print('Input tensor:\n', _input_tensor)
print('Output tensor:\n', _input_tensor.nonzero())
print('Output tensor:\n', _input_tensor.nonzero(as_tuple=True))