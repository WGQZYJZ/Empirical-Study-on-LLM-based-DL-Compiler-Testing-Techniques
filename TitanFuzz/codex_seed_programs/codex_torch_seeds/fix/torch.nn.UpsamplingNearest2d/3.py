'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.UpsamplingNearest2d\ntorch.nn.UpsamplingNearest2d(size=None, scale_factor=None)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 1, 5, 5)
output = nn.UpsamplingNearest2d(scale_factor=2)(input_data)
print(output)