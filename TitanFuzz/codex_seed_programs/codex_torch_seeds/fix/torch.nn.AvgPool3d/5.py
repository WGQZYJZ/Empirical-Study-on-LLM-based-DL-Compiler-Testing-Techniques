'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool3d\ntorch.nn.AvgPool3d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
from torch.nn import AvgPool3d
input = torch.randn(1, 3, 5, 5, 5)
avg_pool = AvgPool3d(kernel_size=3, stride=1)
output = avg_pool(input)
print('input.shape: ', input.shape)
print('output.shape: ', output.shape)
print('output: ', output)