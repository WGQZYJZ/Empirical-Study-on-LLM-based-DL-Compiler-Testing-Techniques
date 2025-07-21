'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyBatchNorm3d\ntorch.nn.LazyBatchNorm3d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
from torch.nn import LazyBatchNorm3d
input_data = torch.randn(1, 2, 3, 4, 5)
out = LazyBatchNorm3d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)(input_data)
print(out)