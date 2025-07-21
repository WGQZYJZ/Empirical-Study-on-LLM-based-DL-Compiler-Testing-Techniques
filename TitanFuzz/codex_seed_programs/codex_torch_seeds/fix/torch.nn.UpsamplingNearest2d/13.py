'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.UpsamplingNearest2d\ntorch.nn.UpsamplingNearest2d(size=None, scale_factor=None)\n'
import torch
import torch.nn as nn
input_data = torch.randn(2, 3, 5, 5)
upsample = nn.UpsamplingNearest2d(scale_factor=2)
output = upsample(input_data)
print('Input: ', input_data)
print('Output: ', output)