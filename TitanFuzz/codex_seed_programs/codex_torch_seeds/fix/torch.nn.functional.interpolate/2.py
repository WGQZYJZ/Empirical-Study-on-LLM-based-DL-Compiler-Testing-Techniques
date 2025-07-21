"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.interpolate\ntorch.nn.functional.interpolate(input, size=None, scale_factor=None, mode='nearest', align_corners=None, recompute_scale_factor=None)\n"
import torch
import torch.nn.functional as F
import torch
input = torch.rand(1, 3, 4, 4)
output = F.interpolate(input, scale_factor=2, mode='nearest')
print(output.shape)
input = torch.rand(1, 3, 4, 4)
output = F.interpolate(input, size=8, mode='nearest')
print(output.shape)