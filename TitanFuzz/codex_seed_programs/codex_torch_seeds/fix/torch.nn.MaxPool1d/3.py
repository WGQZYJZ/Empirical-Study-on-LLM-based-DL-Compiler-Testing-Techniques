'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool1d\ntorch.nn.MaxPool1d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
import torch.nn as nn
input = torch.randn(20, 16, 50)
m = nn.MaxPool1d(3, stride=2)
output = m(input)
print(output.size())