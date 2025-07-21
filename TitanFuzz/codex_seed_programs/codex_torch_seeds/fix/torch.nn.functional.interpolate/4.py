"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.interpolate\ntorch.nn.functional.interpolate(input, size=None, scale_factor=None, mode='nearest', align_corners=None, recompute_scale_factor=None)\n"
import torch
import torch.nn.functional as F
print(torch.__version__)
input = torch.rand(1, 3, 3, 3)
output_size = (5, 5)
output = F.interpolate(input, size=output_size, mode='nearest')
print(output)