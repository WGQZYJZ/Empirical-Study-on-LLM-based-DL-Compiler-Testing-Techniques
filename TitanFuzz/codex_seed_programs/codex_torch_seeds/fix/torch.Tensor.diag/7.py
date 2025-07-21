'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diag\ntorch.Tensor.diag(_input_tensor, diagonal=0)\n'
import torch
import numpy as np
print('Task 1: import PyTorch')
print('PyTorch version: {}'.format(torch.__version__))
print('PyTorch path: {}'.format(torch.__path__))
print('Task 2: Generate input data')
input_tensor = torch.rand(3, 3)
print('input_tensor: {}'.format(input_tensor))
print('Task 3: Call the API torch.Tensor.diag')
output_tensor = torch.Tensor.diag(input_tensor, diagonal=0)
print('output_tensor: {}'.format(output_tensor))