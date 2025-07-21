'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.set_\ntorch.Tensor.set_(_input_tensor, source=None, storage_offset=0, size=None, stride=None)\n'
import torch
import numpy as np
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
_input_tensor = torch.tensor(np.random.rand(3, 3))
print('Input tensor: {}'.format(_input_tensor))
print('Task 3: Call the API torch.Tensor.set_')
_input_tensor.set_(torch.tensor(np.random.rand(3, 3)))
print('Input tensor: {}'.format(_input_tensor))