"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cdist\ntorch.cdist(x1, x2, p=2.0, compute_mode='use_mm_for_euclid_dist_if_necessary')\n"
import torch
import torch.nn as nn
x1 = torch.randn(3, 4)
x2 = torch.randn(5, 4)
dist = torch.cdist(x1, x2, p=2.0, compute_mode='use_mm_for_euclid_dist_if_necessary')
print(dist)
print(dist.shape)
print(dist.dtype)