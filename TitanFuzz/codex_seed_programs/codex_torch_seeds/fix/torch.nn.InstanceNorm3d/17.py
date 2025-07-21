'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.InstanceNorm3d\ntorch.nn.InstanceNorm3d(num_features, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False, device=None, dtype=None)\n'
import torch
from torch.nn import InstanceNorm3d
import numpy as np
print('Task 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('Task 2: Generate input data')
x = np.random.randn(2, 3, 4, 5, 6).astype(np.float32)
x = torch.from_numpy(x)
print('Input tensor: ', x)
print('Task 3: Call the API torch.nn.InstanceNorm3d')
ins_norm3d = InstanceNorm3d(3)
y = ins_norm3d(x)
print('Output tensor: ', y)