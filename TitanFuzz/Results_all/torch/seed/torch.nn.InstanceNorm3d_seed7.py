input = torch.randn(1, 2, 3, 4, 5)
output = torch.nn.InstanceNorm3d(num_features=2, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)(input)