"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cdist\ntorch.cdist(x1, x2, p=2.0, compute_mode='use_mm_for_euclid_dist_if_necessary')\n"
import torch
x1 = torch.randn(4, 3, 5)
x2 = torch.randn(4, 3, 5)
torch.cdist(x1, x2, p=2.0, compute_mode='use_mm_for_euclid_dist_if_necessary')
torch.cdist(x1, x2, p=2.0, compute_mode='donot_use_mm_for_euclid_dist')
torch.cdist(x1, x2, p=2.0, compute_mode='use_mm_for_euclid_dist')
torch.cdist(x1, x2, p=2.0, compute_mode='use_mm_for_euclid_dist_if_necessary')
torch.cdist(x1, x2, p=1.0, compute_mode='use_mm_for_euclid_dist_if_necessary')