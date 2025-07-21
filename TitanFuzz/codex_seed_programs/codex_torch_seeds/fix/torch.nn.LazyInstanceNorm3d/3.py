'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyInstanceNorm3d\ntorch.nn.LazyInstanceNorm3d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(1, 1, 3, 3, 3)
norm = nn.LazyInstanceNorm3d(1, affine=False)
output = norm(input)
print(output)