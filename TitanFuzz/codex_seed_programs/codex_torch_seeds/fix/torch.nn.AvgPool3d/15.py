'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool3d\ntorch.nn.AvgPool3d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
import torch.nn as nn
input_data = torch.arange(1, 49).view(1, 1, 4, 4, 3)
print(input_data)
avg_pool3d = nn.AvgPool3d(kernel_size=(2, 2, 2), stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)
output = avg_pool3d(input_data)
print(output)