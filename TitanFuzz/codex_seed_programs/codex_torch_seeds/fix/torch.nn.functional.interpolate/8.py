"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.interpolate\ntorch.nn.functional.interpolate(input, size=None, scale_factor=None, mode='nearest', align_corners=None, recompute_scale_factor=None)\n"
import torch
import torch
input = torch.randn(1, 1, 4, 4)
print(torch.nn.functional.interpolate(input, size=None, scale_factor=2, mode='nearest', align_corners=None, recompute_scale_factor=None))