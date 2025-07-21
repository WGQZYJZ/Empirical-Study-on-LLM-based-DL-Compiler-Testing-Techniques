"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample\ntorch.nn.functional.upsample(input, size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
import torch.nn.functional as F
in_data = torch.randn(1, 3, 5, 5)
out_data = F.upsample(in_data, scale_factor=2)
print(out_data)