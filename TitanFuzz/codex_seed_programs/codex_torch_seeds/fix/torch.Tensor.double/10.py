'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.double\ntorch.Tensor.double(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
import numpy as np
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
_input_tensor = torch.randn(5, 5, dtype=torch.float32)
print('Input tensor: {}'.format(_input_tensor))
print('Task 3: Call the API torch.Tensor.double')
_output_tensor = torch.Tensor.double(_input_tensor)
print('Output tensor: {}'.format(_output_tensor))