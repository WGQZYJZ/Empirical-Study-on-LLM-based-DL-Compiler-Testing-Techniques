'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GroupNorm\ntorch.nn.GroupNorm(num_groups, num_channels, eps=1e-05, affine=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input = torch.randn((1, 3, 3, 3))
num_groups = 3
num_channels = 3
eps = 1e-05
affine = True
group_norm = nn.GroupNorm(num_groups, num_channels, eps, affine)
output = group_norm(input)
print(output)