'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool3d\ntorch.nn.AdaptiveAvgPool3d(output_size)\n'
import torch
import torch.nn as nn
'\nTask 1:\n'
'\nTask 2:\n'
input = torch.randn(20, 16, 50, 32, 32)
'\nTask 3:\n'
m = nn.AdaptiveAvgPool3d(output_size=(1, 1, 1))
output = m(input)
print(output.size())