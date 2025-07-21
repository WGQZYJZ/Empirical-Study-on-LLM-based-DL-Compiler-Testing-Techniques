'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.conv1d\ntorch.nn.functional.conv1d(input, weight, bias=None, stride=1, padding=0, dilation=1, groups=1)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input = torch.randn(4, 1, 7)
conv1d = F.conv1d(input, torch.randn(1, 1, 3), bias=None, stride=1, padding=0, dilation=1, groups=1)
print(conv1d)