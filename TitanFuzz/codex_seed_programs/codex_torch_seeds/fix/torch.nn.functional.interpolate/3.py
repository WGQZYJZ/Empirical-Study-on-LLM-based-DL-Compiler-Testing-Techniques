"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.interpolate\ntorch.nn.functional.interpolate(input, size=None, scale_factor=None, mode='nearest', align_corners=None, recompute_scale_factor=None)\n"
import torch
import torch.nn.functional as F
import torch
input = torch.rand(1, 1, 2, 2)
output = F.interpolate(input, scale_factor=2, mode='nearest')
print(output)
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pad\ntorch.nn.functional.pad(input, pad, mode='constant', value=0)\n"
import torch
import torch.nn.functional as F
import torch
input = torch.rand(2, 3, 4, 5)
output = F.pad(input, (1, 1, 2, 2))
print(output)