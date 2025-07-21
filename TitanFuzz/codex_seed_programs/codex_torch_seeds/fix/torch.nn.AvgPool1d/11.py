'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool1d\ntorch.nn.AvgPool1d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
import torch.nn as nn
x = torch.randn(1, 1, 4, requires_grad=True)
print(x)
avgpool = nn.AvgPool1d(2, stride=2)
y = avgpool(x)
print(y)