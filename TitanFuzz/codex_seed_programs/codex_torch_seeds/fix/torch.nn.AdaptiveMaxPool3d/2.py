'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool3d\ntorch.nn.AdaptiveMaxPool3d(output_size, return_indices=False)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 1, 8, 8, 8)
pooled = nn.AdaptiveMaxPool3d(output_size=(4, 4, 4))(input)
print(pooled.shape)