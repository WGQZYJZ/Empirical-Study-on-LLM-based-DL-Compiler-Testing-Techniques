"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Conv2d\ntorch.nn.Conv2d(in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True, padding_mode='zeros', device=None, dtype=None)\n"
import torch
import torch.nn as nn
input = torch.randn(1, 1, 5, 5)
conv = nn.Conv2d(in_channels=1, out_channels=1, kernel_size=3, stride=1, padding=0)
print('Parameters: ', list(conv.parameters()))
out = conv(input)
print('Output: ', out)
print('Output Shape: ', out.shape)