'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyBatchNorm3d\ntorch.nn.LazyBatchNorm3d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
x = torch.rand(2, 3, 4, 5, 6)
lazy_batch_norm_3d = nn.LazyBatchNorm3d(3)
output = lazy_batch_norm_3d(x)
print(output)