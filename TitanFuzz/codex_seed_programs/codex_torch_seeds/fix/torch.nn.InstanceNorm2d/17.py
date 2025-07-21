'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.InstanceNorm2d\ntorch.nn.InstanceNorm2d(num_features, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch
input_data = torch.randn(1, 3, 5, 5)
norm_layer = nn.InstanceNorm2d(3)
output = norm_layer(input_data)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LayerNorm\ntorch.nn.LayerNorm(normalized_shape, eps=1e-05, elementwise_affine=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch
input_data = torch.randn(1, 3, 5, 5)
norm_layer = nn.LayerNorm(3)