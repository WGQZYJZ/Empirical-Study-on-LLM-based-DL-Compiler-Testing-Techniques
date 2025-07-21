"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cdist\ntorch.cdist(x1, x2, p=2.0, compute_mode='use_mm_for_euclid_dist_if_necessary')\n"
import torch
import numpy as np
x1 = torch.rand(2, 3)
x2 = torch.rand(2, 3)
print(x1)
print(x2)
print(torch.cdist(x1, x2, p=2.0, compute_mode='use_mm_for_euclid_dist_if_necessary'))
x1 = torch.rand(2, 3)
x2 = torch.rand(3, 3)
print(x1)
print(x2)
print(torch.cdist(x1, x2, p=2.0, compute_mode='use_mm_for_euclid_dist_if_necessary'))
x1 = torch.rand(2, 3)
x2 = torch.rand(2, 3)
print(x1)
print(x2)