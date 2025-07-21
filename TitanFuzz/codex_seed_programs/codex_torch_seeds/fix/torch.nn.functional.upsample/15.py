"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample\ntorch.nn.functional.upsample(input, size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
import torch.nn as nn
import torch.nn.functional as F
input = torch.randn(1, 1, 3, 3)
upsample = F.upsample(input, scale_factor=2, mode='bilinear')
print('input: ', input)
print('upsample: ', upsample)