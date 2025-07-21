'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.InstanceNorm3d\ntorch.nn.InstanceNorm3d(num_features, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 3, 5, 5, 5)
instance_norm = nn.InstanceNorm3d(3, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)
output = instance_norm(input)
print(output)