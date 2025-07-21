'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool1d\ntorch.nn.AdaptiveAvgPool1d(output_size)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 1, 5)
m = nn.AdaptiveAvgPool1d(output_size=1)
output = m(input)
print(output)