'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool3d\ntorch.nn.AdaptiveMaxPool3d(output_size, return_indices=False)\n'
import torch
import torch.nn as nn
input_data = torch.randn(20, 16, 50, 32, 45)
adaptive_max_pool3d = nn.AdaptiveMaxPool3d(output_size=(5, 4, 3))
output = adaptive_max_pool3d(input_data)
print(output.shape)
adaptive_max_pool3d = nn.AdaptiveMaxPool3d(output_size=(5, 4, 3), return_indices=True)
(output, indices) = adaptive_max_pool3d(input_data)
print(output.shape, indices.shape)