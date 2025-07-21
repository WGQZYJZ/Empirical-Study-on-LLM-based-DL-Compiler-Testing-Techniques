"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.interpolate\ntorch.nn.functional.interpolate(input, size=None, scale_factor=None, mode='nearest', align_corners=None, recompute_scale_factor=None)\n"
import torch
import torch.nn.functional as F
import torch
input_data = torch.randn(1, 1, 3, 3)
output_data = F.interpolate(input_data, scale_factor=2, mode='nearest')
print(output_data)
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.interpolate\ntorch.nn.functional.interpolate(input, size=None, scale_factor=None, mode='nearest', align_corners=None, recompute_scale_factor=None)\n"
import torch
import torch.nn.functional as F
import torch
input_data = torch.randn(1, 1, 3, 3)
output_data = F.interpolate(input_data, size=5, mode='nearest')
print(output_data)