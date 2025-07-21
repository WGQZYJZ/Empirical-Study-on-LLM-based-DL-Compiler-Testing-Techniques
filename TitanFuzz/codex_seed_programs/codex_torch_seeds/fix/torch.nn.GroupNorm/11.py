'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GroupNorm\ntorch.nn.GroupNorm(num_groups, num_channels, eps=1e-05, affine=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input = torch.randn(16, 4, 5, 5)
group_norm = nn.GroupNorm(2, 4)
output = group_norm(input)
print(output)