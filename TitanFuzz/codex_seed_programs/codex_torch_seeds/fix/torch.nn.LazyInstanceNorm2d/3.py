'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyInstanceNorm2d\ntorch.nn.LazyInstanceNorm2d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
'\nTask 2: Generate input data\n'
input = torch.randn(1, 3, 4, 4, requires_grad=True)
'\nTask 3: Call the API torch.nn.LazyInstanceNorm2d\ntorch.nn.LazyInstanceNorm2d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
m = nn.LazyInstanceNorm2d(3)
m = nn.LazyInstanceNorm2d(3, affine=True)
m = nn.LazyInstanceNorm2d(3, affine=True, track_running_stats=False)
m = nn.LazyInstanceNorm2d(3, affine=True, track_running_stats=False, device='cpu')