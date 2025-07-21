'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sum\ntorch.Tensor.sum(_input_tensor, dim=None, keepdim=False, dtype=None)\n'
import torch
import numpy as np
_input_tensor = torch.rand(2, 3)
print('Input tensor: \n', _input_tensor)
_output_tensor = _input_tensor.sum(dim=0)
print('Output tensor: \n', _output_tensor)
_input_numpy = _input_tensor.numpy()
_output_numpy = np.sum(_input_numpy, axis=0)
print('Output numpy: \n', _output_numpy)