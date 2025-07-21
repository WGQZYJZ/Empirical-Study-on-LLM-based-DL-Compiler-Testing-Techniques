'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.InstanceNorm3d\ntorch.nn.InstanceNorm3d(num_features, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
import torch.nn as nn
import torch.nn.functional as F
input_x = torch.randn(1, 3, 3, 3, 3)
print(input_x)
'\ntorch.nn.InstanceNorm3d(num_features, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False, device=None, dtype=None)\n'
instance_norm_3d = nn.InstanceNorm3d(num_features=3, affine=True)
output = instance_norm_3d(input_x)
print(output)
print(instance_norm_3d.weight)
print(instance_norm_3d.bias)