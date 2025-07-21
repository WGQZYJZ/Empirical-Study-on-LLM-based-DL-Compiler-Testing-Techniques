'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool2d\ntorch.nn.MaxPool2d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
import torch.nn as nn
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.Tensor(1, 1, 4, 4)
input[0][0] = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print('Input data:')
print(input)
print('Task 3: Call the API torch.nn.MaxPool2d')
maxpool2d = nn.MaxPool2d(2, stride=1, padding=0)
output = maxpool2d(input)
print('Output data:')
print(output)