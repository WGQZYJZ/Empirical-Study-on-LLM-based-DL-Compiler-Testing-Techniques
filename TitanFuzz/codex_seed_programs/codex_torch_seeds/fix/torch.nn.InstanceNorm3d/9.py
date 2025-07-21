'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.InstanceNorm3d\ntorch.nn.InstanceNorm3d(num_features, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch
input = torch.randn(2, 3, 4, 5, 6)
module = nn.InstanceNorm3d(3)
output = module(input)
print(output)