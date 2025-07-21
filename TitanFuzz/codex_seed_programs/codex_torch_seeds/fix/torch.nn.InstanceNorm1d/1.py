'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.InstanceNorm1d\ntorch.nn.InstanceNorm1d(num_features, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False, device=None, dtype=None)\n'
import torch
import numpy as np
x = np.random.rand(10, 3, 10)
x = torch.tensor(x, dtype=torch.float32)
torch.nn.InstanceNorm1d(num_features=3, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)