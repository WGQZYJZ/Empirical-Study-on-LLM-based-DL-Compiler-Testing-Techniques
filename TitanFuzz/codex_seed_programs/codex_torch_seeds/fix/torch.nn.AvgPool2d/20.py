'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool2d\ntorch.nn.AvgPool2d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
import torch.nn as nn
input = torch.randn(20, 16, 50, 32)
avgpool = nn.AvgPool2d(2, stride=1)
output = avgpool(input)
print(output.size())