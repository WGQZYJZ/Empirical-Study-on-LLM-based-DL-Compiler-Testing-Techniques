'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumsum\ntorch.Tensor.cumsum(_input_tensor, dim, dtype=None)\n'
import torch
import torch
_input_tensor = torch.randn(2, 3, 4)
print('Input tensor: {}'.format(_input_tensor))
_output_tensor = _input_tensor.cumsum(dim=1)
print('Output tensor: {}'.format(_output_tensor))