'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool2d\ntorch.nn.AdaptiveAvgPool2d(output_size)\n'
import torch
from torch.nn import AdaptiveAvgPool2d
input = torch.randn(1, 16, 5, 5)
pool = AdaptiveAvgPool2d((3, 3))
output = pool(input)
print(output)