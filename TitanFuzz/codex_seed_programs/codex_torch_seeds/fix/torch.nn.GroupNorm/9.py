'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GroupNorm\ntorch.nn.GroupNorm(num_groups, num_channels, eps=1e-05, affine=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
print('Task 1: import PyTorch')
print('PyTorch version: {}'.format(torch.__version__))
print('Task 2: Generate input data')
input_data = torch.randn(1, 3, 3, 3)
print('input data: {}'.format(input_data))
print('Task 3: Call the API torch.nn.GroupNorm')
group_norm = nn.GroupNorm(3, 3)
print('group_norm: {}'.format(group_norm))
print('output: {}'.format(group_norm(input_data)))