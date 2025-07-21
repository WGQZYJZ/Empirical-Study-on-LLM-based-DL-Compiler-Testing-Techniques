'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool1d\ntorch.nn.MaxPool1d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 1, 10)
print('Input data: ', input_data)
max_pool_1d = nn.MaxPool1d(kernel_size=2, stride=1, padding=0)
output = max_pool_1d(input_data)
print('Output: ', output)