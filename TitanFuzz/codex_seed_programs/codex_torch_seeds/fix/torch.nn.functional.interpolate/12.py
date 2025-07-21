"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.interpolate\ntorch.nn.functional.interpolate(input, size=None, scale_factor=None, mode='nearest', align_corners=None, recompute_scale_factor=None)\n"
import torch
from torch.nn.functional import interpolate
input = torch.randn(1, 1, 5, 5)
output = interpolate(input, size=(10, 10))
print(output)