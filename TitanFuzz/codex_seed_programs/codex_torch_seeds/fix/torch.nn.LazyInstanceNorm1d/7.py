'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyInstanceNorm1d\ntorch.nn.LazyInstanceNorm1d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch
input_data = torch.randn(20, 16, 50)
layer = nn.LazyInstanceNorm1d(16, affine=False)
output = layer(input_data)
print(output)