input_data = torch.randn(2, 3, 4, 5)
norm_layer = torch.nn.LazyInstanceNorm2d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)
output = norm_layer(input_data)