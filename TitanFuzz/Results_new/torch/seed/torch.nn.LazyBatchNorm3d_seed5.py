input_data = torch.randn(3, 5, 4, 3, 2)
bn3d = torch.nn.LazyBatchNorm3d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)