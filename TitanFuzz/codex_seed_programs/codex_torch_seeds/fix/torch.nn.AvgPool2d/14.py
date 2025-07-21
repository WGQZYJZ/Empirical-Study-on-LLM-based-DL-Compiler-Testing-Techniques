'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool2d\ntorch.nn.AvgPool2d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input_data = torch.randn(1, 1, 7, 7)
avg_pool_2d = nn.AvgPool2d(3, stride=2, padding=1)
output_data = avg_pool_2d(input_data)
print('input_data: ', input_data)
print('output_data: ', output_data)