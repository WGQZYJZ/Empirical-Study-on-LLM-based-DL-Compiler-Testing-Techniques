'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyBatchNorm3d\ntorch.nn.LazyBatchNorm3d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input = torch.randn(32, 3, 8, 8, 8)
batch_norm = nn.LazyBatchNorm3d(3)
output = batch_norm(input)
print(output)