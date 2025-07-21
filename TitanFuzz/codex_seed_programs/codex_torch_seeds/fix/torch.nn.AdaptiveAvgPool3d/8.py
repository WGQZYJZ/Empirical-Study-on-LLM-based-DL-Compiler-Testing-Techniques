'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool3d\ntorch.nn.AdaptiveAvgPool3d(output_size)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 3, 5, 5, 5)
avg_pool3d = nn.AdaptiveAvgPool3d((3, 3, 3))
output = avg_pool3d(input)
print(output.shape)