'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool3d\ntorch.nn.AdaptiveMaxPool3d(output_size, return_indices=False)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 2, 10, 10, 10)
output_size = (5, 5, 5)
adaptive_max_pool3d = nn.AdaptiveMaxPool3d(output_size)
output = adaptive_max_pool3d(input)
print(output)