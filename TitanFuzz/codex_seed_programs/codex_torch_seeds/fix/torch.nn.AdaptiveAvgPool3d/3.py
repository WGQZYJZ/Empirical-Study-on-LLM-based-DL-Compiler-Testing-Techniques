'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool3d\ntorch.nn.AdaptiveAvgPool3d(output_size)\n'
import torch
from torch.nn import AdaptiveAvgPool3d
input = torch.randn(1, 2, 3, 4, 5)
adaptive_avg_pool_3d = AdaptiveAvgPool3d(output_size=(2, 2, 2))
output = adaptive_avg_pool_3d(input)
print('input size:', input.size())
print('output size:', output.size())