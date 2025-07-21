"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Upsample\ntorch.nn.Upsample(size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
input = torch.ones(1, 1, 3, 3)
upsample = nn.Upsample(size=(5, 5), mode='nearest')
output = upsample(input)
print('input.size() = ', input.size())
print('output.size() = ', output.size())