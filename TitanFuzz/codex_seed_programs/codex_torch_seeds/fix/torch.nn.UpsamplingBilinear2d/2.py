'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.UpsamplingBilinear2d\ntorch.nn.UpsamplingBilinear2d(size=None, scale_factor=None)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 1, 3, 3)
print(input)
upsample = nn.UpsamplingBilinear2d(scale_factor=2)
output = upsample(input)
print(output)
upsample = nn.UpsamplingBilinear2d(size=(5, 5))
output = upsample(input)
print(output)