'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool2d\ntorch.nn.MaxPool2d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
import torch.nn as nn
print('Task 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('Task 2: Generate input data')
input_size = (1, 1, 4, 4)
input_data = torch.randn(input_size)
print('Input data: ', input_data)
print('Task 3: Call the API torch.nn.MaxPool2d')
max_pooling = nn.MaxPool2d(kernel_size=2, stride=2)
output = max_pooling(input_data)
print('Output: ', output)