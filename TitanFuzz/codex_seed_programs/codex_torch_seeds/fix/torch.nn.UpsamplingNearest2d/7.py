'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.UpsamplingNearest2d\ntorch.nn.UpsamplingNearest2d(size=None, scale_factor=None)\n'
import torch
from torch import nn
input_data = torch.randn(1, 1, 3, 3)
upsampling_nearest2d = nn.UpsamplingNearest2d(scale_factor=2)
output_data = upsampling_nearest2d(input_data)
print('output_data: ', output_data)