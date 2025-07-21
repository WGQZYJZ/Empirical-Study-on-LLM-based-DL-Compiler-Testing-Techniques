"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Upsample\ntorch.nn.Upsample(size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
import torch.nn as nn
input = torch.randn(2, 3, 5, 5)
upsample = nn.Upsample(size=(5, 10), mode='nearest')
output = upsample(input)
print(output.size())