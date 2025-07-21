'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool3d\ntorch.nn.functional.avg_pool3d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input = torch.randn(1, 2, 6, 6, 6)
output = F.avg_pool3d(input, kernel_size=2, stride=2, padding=0)
print(output)
output = F.avg_pool3d(input, kernel_size=2, stride=2, padding=1)
print(output)
output = F.avg_pool3d(input, kernel_size=2, stride=2, padding=1, ceil_mode=True)
print(output)
output = F.avg_pool3d(input, kernel_size=2, stride=2, padding=1, count_include_pad=False)
print(output)