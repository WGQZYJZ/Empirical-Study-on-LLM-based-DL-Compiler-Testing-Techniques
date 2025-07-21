'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool1d\ntorch.nn.AvgPool1d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 1, 5)
pool = nn.AvgPool1d(3, stride=1, padding=0)
output = pool(input_data)
print('input_data: ', input_data)
print('output: ', output)