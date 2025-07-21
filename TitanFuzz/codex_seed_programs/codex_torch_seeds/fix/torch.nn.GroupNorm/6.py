'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GroupNorm\ntorch.nn.GroupNorm(num_groups, num_channels, eps=1e-05, affine=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input = torch.randn(20, 16, 50, 32)
out = nn.GroupNorm(4, 16, eps=1e-05).forward(input)
out = nn.GroupNorm(4, 16, eps=1e-05, affine=True).forward(input)
print('out.shape: ', out.shape)