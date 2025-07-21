'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool2d\ntorch.nn.MaxPool2d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 1, 4, 4)
print('Input data: ', input_data)
max_pool2d = nn.MaxPool2d(2, stride=2)
output = max_pool2d(input_data)
print('Output: ', output)