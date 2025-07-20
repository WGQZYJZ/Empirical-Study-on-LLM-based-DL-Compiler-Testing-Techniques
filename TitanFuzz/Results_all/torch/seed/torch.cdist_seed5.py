x1 = torch.rand(100, 3)
x2 = torch.rand(100, 3)
dist = torch.cdist(x1, x2, p=2.0, compute_mode='use_mm_for_euclid_dist_if_necessary')