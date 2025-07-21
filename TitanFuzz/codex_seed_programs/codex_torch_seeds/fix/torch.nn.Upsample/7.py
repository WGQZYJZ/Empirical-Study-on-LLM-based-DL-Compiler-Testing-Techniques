"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Upsample\ntorch.nn.Upsample(size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
import torch.nn as nn
input = torch.randn(1, 1, 3, 3)
print(input)
upsample = nn.Upsample(scale_factor=2)
print(upsample(input))