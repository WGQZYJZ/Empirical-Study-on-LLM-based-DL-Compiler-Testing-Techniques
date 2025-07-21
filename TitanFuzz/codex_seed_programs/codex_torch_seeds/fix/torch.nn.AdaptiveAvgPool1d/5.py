'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool1d\ntorch.nn.AdaptiveAvgPool1d(output_size)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(1, 1, 4)
print(input)
pooling = nn.AdaptiveAvgPool1d(2)
output = pooling(input)
print(output)