'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.UpsamplingBilinear2d\ntorch.nn.UpsamplingBilinear2d(size=None, scale_factor=None)\n'
import torch
import torch.nn as nn
import numpy as np
input_data = torch.randn(1, 1, 3, 3)
print('Input data:')
print(input_data)
upsampling = nn.UpsamplingBilinear2d(size=(4, 4), scale_factor=None)
output_data = upsampling(input_data)
print('Output data:')
print(output_data)