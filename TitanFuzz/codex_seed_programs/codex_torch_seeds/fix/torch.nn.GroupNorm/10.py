'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GroupNorm\ntorch.nn.GroupNorm(num_groups, num_channels, eps=1e-05, affine=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import numpy as np
x = torch.randn(16, 32, 32, 32)
x = nn.GroupNorm(4, 32)(x)
print(x.shape)