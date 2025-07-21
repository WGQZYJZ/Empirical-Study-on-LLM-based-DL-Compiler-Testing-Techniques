'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool2d\ntorch.nn.functional.avg_pool2d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input_data = torch.randn(1, 1, 5, 5)
output = F.avg_pool2d(input_data, kernel_size=3, stride=1, padding=1)
print('output:', output)
output = F.avg_pool2d(input_data, kernel_size=3, stride=1, padding=1, count_include_pad=False)
print('output:', output)
output = F.avg_pool2d(input_data, kernel_size=3, stride=1, padding=1, ceil_mode=True)
print('output:', output)
output = F.avg_pool2d(input_data, kernel_size=3, stride=1, padding=1, divisor_override=4)
print('output:', output)