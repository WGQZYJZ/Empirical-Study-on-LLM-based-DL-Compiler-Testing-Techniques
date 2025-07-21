'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.InstanceNorm1d\ntorch.nn.InstanceNorm1d(num_features, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import numpy as np
input_data = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
input_data = input_data.astype(np.float32)
input_data = torch.from_numpy(input_data)
instance_norm = nn.InstanceNorm1d(num_features=5, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)
output = instance_norm(input_data)
print(output)