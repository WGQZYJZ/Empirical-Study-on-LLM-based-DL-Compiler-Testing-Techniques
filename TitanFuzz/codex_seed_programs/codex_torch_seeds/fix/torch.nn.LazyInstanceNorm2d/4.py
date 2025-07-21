'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyInstanceNorm2d\ntorch.nn.LazyInstanceNorm2d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input_data = torch.randn(1, 3, 10, 10)
instance_norm2d = nn.LazyInstanceNorm2d(3, affine=True)
output_data = instance_norm2d(input_data)
print(output_data)