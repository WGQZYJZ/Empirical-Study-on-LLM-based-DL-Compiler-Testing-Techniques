'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyInstanceNorm2d\ntorch.nn.LazyInstanceNorm2d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
from torch import nn
input_data = torch.randn(2, 3, 4, 4)
norm = nn.LazyInstanceNorm2d(3, affine=False)
output = norm(input_data)
print(output)
norm = nn.LazyInstanceNorm2d(3, affine=True)
output = norm(input_data)
print(output)