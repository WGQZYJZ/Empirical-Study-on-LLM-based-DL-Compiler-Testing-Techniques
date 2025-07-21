'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyBatchNorm3d\ntorch.nn.LazyBatchNorm3d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
x = torch.randn((2, 3, 4, 5, 6))
lazy_bn = torch.nn.LazyBatchNorm3d(3)
lazy_bn(x)