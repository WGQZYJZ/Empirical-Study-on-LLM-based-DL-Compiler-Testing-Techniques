"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.interpolate\ntorch.nn.functional.interpolate(input, size=None, scale_factor=None, mode='nearest', align_corners=None, recompute_scale_factor=None)\n"
import torch
import torch.nn.functional as F
import torch
input_data = torch.rand(1, 1, 3, 3)
output = F.interpolate(input_data, size=3, mode='nearest')
print(input_data)
print(output)