'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample_bilinear\ntorch.nn.functional.upsample_bilinear(input, size=None, scale_factor=None)\n'
import torch
from torch.nn.functional import upsample_bilinear
input = torch.randn(1, 1, 2, 2)
print(input)
input = torch.randn(1, 1, 2, 2)
print(input)
output = upsample_bilinear(input, scale_factor=2)
print(output)