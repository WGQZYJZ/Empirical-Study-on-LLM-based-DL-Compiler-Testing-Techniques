"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Upsample\ntorch.nn.Upsample(size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
import torch.nn as nn
import torch.nn.functional as F
input = torch.rand(1, 1, 4, 4)
upsample = nn.Upsample(scale_factor=2, mode='nearest')
output = upsample(input)
print(input)
print(output)