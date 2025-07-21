'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LayerNorm\ntorch.nn.LayerNorm(normalized_shape, eps=1e-05, elementwise_affine=True, device=None, dtype=None)\n'
import torch
from torch.nn import LayerNorm
input_data = torch.randn(20, 5, 10, 10)
norm_layer = LayerNorm(normalized_shape=[10, 10])
output = norm_layer(input_data)
print(output.size())
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GroupNorm\ntorch.nn.GroupNorm(num_groups, num_channels, eps=1e-05, affine=True, track_running_stats=True)\n'
import torch
from torch.nn import GroupNorm
input_data = torch.randn(20, 16, 10, 10)
norm_layer = GroupNorm(num_groups=4, num_channels=16)
output = norm_layer(input_data)
print(output.size())