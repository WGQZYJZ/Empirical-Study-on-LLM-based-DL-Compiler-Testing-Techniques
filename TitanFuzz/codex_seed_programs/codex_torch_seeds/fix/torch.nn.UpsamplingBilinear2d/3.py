'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.UpsamplingBilinear2d\ntorch.nn.UpsamplingBilinear2d(size=None, scale_factor=None)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 1, 5, 5)
upsample_bilinear2d = nn.UpsamplingBilinear2d(scale_factor=2)
output = upsample_bilinear2d(input)
print(output)