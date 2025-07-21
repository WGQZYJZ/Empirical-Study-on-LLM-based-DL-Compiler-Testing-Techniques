'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.conv1d\ntorch.nn.functional.conv1d(input, weight, bias=None, stride=1, padding=0, dilation=1, groups=1)\n'
import torch
import torch.nn.functional as F
import torch
import torch.nn as nn
import torch.optim as optim
input = torch.randn(1, 1, 3)
print('input:', input)
weight = torch.randn(2, 1, 3)
print('weight:', weight)
output = F.conv1d(input, weight, padding=1)
print('output:', output)