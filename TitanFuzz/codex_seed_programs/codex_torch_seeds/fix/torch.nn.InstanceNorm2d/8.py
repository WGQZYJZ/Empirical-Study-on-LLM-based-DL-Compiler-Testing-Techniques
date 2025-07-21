'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.InstanceNorm2d\ntorch.nn.InstanceNorm2d(num_features, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import numpy as np
input_data = np.random.random((1, 3, 3, 3))
input_data = torch.tensor(input_data, dtype=torch.float32)
instance_norm = nn.InstanceNorm2d(3)
output = instance_norm(input_data)
print(output)