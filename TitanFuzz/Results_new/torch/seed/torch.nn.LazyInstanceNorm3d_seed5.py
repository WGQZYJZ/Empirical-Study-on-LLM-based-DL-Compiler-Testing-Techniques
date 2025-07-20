input = torch.randn(4, 4, 4, 4, 4)
layer = torch.nn.LazyInstanceNorm3d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)
output = layer(input)