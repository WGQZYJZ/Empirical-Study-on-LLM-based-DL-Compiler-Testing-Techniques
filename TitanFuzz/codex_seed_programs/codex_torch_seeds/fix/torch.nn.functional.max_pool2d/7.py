'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_pool2d\ntorch.nn.functional.max_pool2d(input, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
print('Task 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('PyTorch location: ', torch.__file__)
print('Task 2: Generate input data')
input = torch.randn(1, 1, 3, 3, requires_grad=True)
print('Input shape: ', input.shape)
print('Input data: \n', input)
print('Task 3: Call the API torch.nn.functional.max_pool2d')
output = F.max_pool2d(input, kernel_size=2, stride=2)
print('Output shape: ', output.shape)
print('Output data: \n', output)