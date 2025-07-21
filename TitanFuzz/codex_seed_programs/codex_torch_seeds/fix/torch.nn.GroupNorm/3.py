'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GroupNorm\ntorch.nn.GroupNorm(num_groups, num_channels, eps=1e-05, affine=True, device=None, dtype=None)\n'
import torch
from torch.nn import GroupNorm
from torch import nn
input = torch.randn(20, 16, 50, 32)
out = GroupNorm(num_groups=4, num_channels=16)(input)
print(out.shape)