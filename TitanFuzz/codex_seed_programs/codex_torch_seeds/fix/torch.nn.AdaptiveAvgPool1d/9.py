'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool1d\ntorch.nn.AdaptiveAvgPool1d(output_size)\n'
import torch
from torch.nn import AdaptiveAvgPool1d
input = torch.randn(1, 64, 8)
m = AdaptiveAvgPool1d(4)
output = m(input)
print(output.shape)