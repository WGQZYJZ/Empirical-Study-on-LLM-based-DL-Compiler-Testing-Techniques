'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LayerNorm\ntorch.nn.LayerNorm(normalized_shape, eps=1e-05, elementwise_affine=True, device=None, dtype=None)\n'
import torch
from torch import nn
input = torch.randn(20, 5, 10, 10)
norm = nn.LayerNorm(input.size()[1:])
output = norm(input)
print(output.size())
'\ntorch.nn.GroupNorm(num_groups, num_channels, eps=1e-05, affine=True, track_running_stats=True)\n'
input = torch.randn(20, 16, 50, 32)
norm = nn.GroupNorm(4, 16)
output = norm(input)
print(output.size())