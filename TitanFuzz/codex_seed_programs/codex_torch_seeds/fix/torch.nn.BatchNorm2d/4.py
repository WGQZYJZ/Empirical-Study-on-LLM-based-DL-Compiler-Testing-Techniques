'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm2d\ntorch.nn.BatchNorm2d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import numpy as np
batch_size = 4
num_features = 3
input_data = torch.randn(batch_size, num_features, 2, 2)
bn = nn.BatchNorm2d(num_features)
print('weight:', bn.weight.data)
print('bias:', bn.bias.data)
output = bn(input_data)
print('output:', output)