'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool3d\ntorch.nn.functional.avg_pool3d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input = torch.randn(1, 1, 3, 3, 3)
print('input:', input)
output = F.avg_pool3d(input, (2, 2, 2))
print('output:', output)