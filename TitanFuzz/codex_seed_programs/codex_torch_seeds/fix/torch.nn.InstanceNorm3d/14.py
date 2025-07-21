'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.InstanceNorm3d\ntorch.nn.InstanceNorm3d(num_features, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_data = torch.rand(1, 1, 3, 3, 3)
print('Input data:\n', input_data)
instance_norm3d = nn.InstanceNorm3d(1, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)
output_data = instance_norm3d(input_data)
print('Output data:\n', output_data)