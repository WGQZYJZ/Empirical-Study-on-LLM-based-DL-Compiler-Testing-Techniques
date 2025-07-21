'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool2d\ntorch.nn.AdaptiveAvgPool2d(output_size)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 1, 8, 8)
avg_pool = nn.AdaptiveAvgPool2d(output_size=4)
output = avg_pool(input)
print(output)