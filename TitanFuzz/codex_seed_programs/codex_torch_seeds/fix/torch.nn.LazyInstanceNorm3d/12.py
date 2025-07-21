'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyInstanceNorm3d\ntorch.nn.LazyInstanceNorm3d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch
input_data = torch.randn(1, 3, 4, 4, 4)
norm = nn.LazyInstanceNorm3d(3, affine=False)
norm(input_data)