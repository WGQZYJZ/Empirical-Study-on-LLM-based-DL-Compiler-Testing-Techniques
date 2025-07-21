'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool2d\ntorch.nn.functional.avg_pool2d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input_data = torch.randn(1, 1, 4, 4)
print('input_data: \n', input_data)
output_data = F.avg_pool2d(input_data, kernel_size=2, stride=2)
print('output_data: \n', output_data)