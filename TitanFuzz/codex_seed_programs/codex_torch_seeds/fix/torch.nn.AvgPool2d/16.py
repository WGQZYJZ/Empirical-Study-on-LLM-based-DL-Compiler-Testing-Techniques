'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool2d\ntorch.nn.AvgPool2d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(3, 3, 3, 3)
avg_pool2d = nn.AvgPool2d(kernel_size=3, stride=2, padding=1)
output = avg_pool2d(input)
print(output)