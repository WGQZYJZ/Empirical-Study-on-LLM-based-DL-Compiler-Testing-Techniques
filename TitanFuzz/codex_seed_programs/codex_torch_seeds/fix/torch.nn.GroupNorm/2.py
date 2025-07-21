'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GroupNorm\ntorch.nn.GroupNorm(num_groups, num_channels, eps=1e-05, affine=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input = torch.randn(20, 16, 50, 32)
norm = nn.GroupNorm(4, 16)
output = norm(input)
print('Input:', input.shape)
print('Output:', output.shape)