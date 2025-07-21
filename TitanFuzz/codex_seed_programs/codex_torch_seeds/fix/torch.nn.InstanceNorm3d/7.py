'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.InstanceNorm3d\ntorch.nn.InstanceNorm3d(num_features, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input = torch.randn(4, 3, 3, 3, 3)
print(input.size())
norm = nn.InstanceNorm3d(3)
output = norm(input)
print(output.size())