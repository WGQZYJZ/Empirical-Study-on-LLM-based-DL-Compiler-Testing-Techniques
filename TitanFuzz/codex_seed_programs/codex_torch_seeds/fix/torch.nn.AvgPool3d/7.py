'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool3d\ntorch.nn.AvgPool3d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 1, 8, 8, 8)
avgpool3d = nn.AvgPool3d(kernel_size=3, stride=1, padding=0)
output = avgpool3d(input_data)
print('input_data: ', input_data)
print('output: ', output)