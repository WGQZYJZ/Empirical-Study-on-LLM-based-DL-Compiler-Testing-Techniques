"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cdist\ntorch.cdist(x1, x2, p=2.0, compute_mode='use_mm_for_euclid_dist_if_necessary')\n"
import torch
import torch
x1 = torch.rand(100, 128)
x2 = torch.rand(200, 128)
dist = torch.cdist(x1, x2)
print(dist.shape)