'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool3d\ntorch.nn.MaxPool3d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 1, 5, 5, 5)
maxpool3d = nn.MaxPool3d(kernel_size=2, stride=2)
output = maxpool3d(input)
print(output)