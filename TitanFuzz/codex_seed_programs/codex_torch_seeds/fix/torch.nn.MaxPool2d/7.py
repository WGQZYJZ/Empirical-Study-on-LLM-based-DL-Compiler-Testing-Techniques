'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool2d\ntorch.nn.MaxPool2d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 1, 5, 5)
print(input)
pool = nn.MaxPool2d(2, stride=2)
output = pool(input)
print(output)