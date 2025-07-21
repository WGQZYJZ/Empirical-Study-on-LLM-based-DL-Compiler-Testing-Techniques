'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout3d\ntorch.nn.Dropout3d(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input = torch.randn(20, 16, 50, 40, 30)
m = nn.Dropout3d(p=0.5, inplace=False)
output = m(input)
print('input size:', input.size())
print('output size:', output.size())