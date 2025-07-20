x1 = torch.randn(3, 4)
x2 = torch.randn(5, 4)
dist = torch.cdist(x1, x2, p=2.0, compute_mode='use_mm_for_euclid_dist_if_necessary')