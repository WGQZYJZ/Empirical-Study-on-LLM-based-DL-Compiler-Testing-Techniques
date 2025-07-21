'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyInstanceNorm1d\ntorch.nn.LazyInstanceNorm1d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input = torch.randn(3, 2, 3)
norm = nn.LazyInstanceNorm1d(3)
output = norm(input)
print(output)