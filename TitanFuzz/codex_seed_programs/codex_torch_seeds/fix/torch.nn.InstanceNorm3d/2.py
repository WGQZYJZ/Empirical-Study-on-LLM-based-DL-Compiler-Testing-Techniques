'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.InstanceNorm3d\ntorch.nn.InstanceNorm3d(num_features, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import numpy as np
input_data = np.random.randn(1, 3, 4, 4, 4)
input_data = torch.tensor(input_data)
instance_norm3d = nn.InstanceNorm3d(3)
output = instance_norm3d(input_data)
print(output)