'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm2d\ntorch.nn.BatchNorm2d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import numpy as np
import torch
input = torch.randn(1, 3, 2, 2)
bn = torch.nn.BatchNorm2d(3)
output = bn(input)
print(output)