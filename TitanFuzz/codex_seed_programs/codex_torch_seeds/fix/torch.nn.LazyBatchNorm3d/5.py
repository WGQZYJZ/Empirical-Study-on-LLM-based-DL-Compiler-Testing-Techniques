'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyBatchNorm3d\ntorch.nn.LazyBatchNorm3d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input_data = torch.randn(1, 3, 2, 4, 5)
bn = nn.LazyBatchNorm3d(3)
output_data = bn(input_data)
print(output_data)