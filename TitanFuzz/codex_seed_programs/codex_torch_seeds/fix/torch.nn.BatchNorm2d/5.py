'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm2d\ntorch.nn.BatchNorm2d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import numpy as np
batch_size = 2
num_features = 3
height = 4
width = 5
input = torch.randn(batch_size, num_features, height, width)
bn = nn.BatchNorm2d(num_features)
output = bn(input)
print(output.shape)