'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool3d\ntorch.nn.AdaptiveAvgPool3d(output_size)\n'
import torch
from torch.nn import AdaptiveAvgPool3d
input = torch.randn(1, 64, 8, 9, 10)
m = AdaptiveAvgPool3d((4, 5, 6))
output = m(input)
print(output.shape)