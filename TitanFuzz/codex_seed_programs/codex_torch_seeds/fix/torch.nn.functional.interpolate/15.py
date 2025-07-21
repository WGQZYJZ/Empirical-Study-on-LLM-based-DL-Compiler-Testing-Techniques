"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.interpolate\ntorch.nn.functional.interpolate(input, size=None, scale_factor=None, mode='nearest', align_corners=None, recompute_scale_factor=None)\n"
import torch
import torch.nn.functional as F
import torch
x = torch.randn(1, 3, 5, 5)
F.interpolate(x, size=(7, 7), mode='bilinear')
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pad\ntorch.nn.functional.pad(input, pad, mode='constant', value=0, recompute_scale_factor=None)\n"
import torch
import torch.nn.functional as F
import torch
x = torch.randn(1, 3, 5, 5)
F.pad(x, (2, 2, 2, 2))