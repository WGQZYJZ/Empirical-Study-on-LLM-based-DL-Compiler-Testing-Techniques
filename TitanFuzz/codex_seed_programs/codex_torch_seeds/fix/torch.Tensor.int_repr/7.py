'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.int_repr\ntorch.Tensor.int_repr(_input_tensor)\n'
import torch
import numpy as np
_input_tensor = torch.randn(2, 3)
_output = _input_tensor.int_repr()
print('Input tensor: {}'.format(_input_tensor))
print('Output tensor: {}'.format(_output))