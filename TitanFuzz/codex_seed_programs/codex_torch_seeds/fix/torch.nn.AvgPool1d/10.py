'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool1d\ntorch.nn.AvgPool1d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
import torch.nn as nn
input = torch.randn(20, 16, 50)
avg_pool1d = nn.AvgPool1d(kernel_size=5, stride=2, ceil_mode=False)
output = avg_pool1d(input)
print(output.size())
avg_pool1d = nn.AvgPool1d(kernel_size=5, stride=2, padding=1, ceil_mode=False)
output = avg_pool1d(input)
print(output.size())
avg_pool1d = nn.AvgPool1d(kernel_size=5, stride=2, ceil_mode=True)
output = avg_pool1d(input)