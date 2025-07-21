'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.UpsamplingNearest2d\ntorch.nn.UpsamplingNearest2d(size=None, scale_factor=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
x = torch.randn(1, 1, 3, 3)
print('Input data: ', x)
upsample = nn.UpsamplingNearest2d(scale_factor=2)
output = upsample(x)
print('Output: ', output)