'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyInstanceNorm1d\ntorch.nn.LazyInstanceNorm1d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
from torch.nn import LazyInstanceNorm1d
input_data = torch.rand(1, 3, 10)
layer = LazyInstanceNorm1d(3)
output = layer(input_data)
print(output)