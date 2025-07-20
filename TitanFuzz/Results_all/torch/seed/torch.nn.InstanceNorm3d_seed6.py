input_data = torch.randn(20, 3, 32, 32, 32)
output = torch.nn.InstanceNorm3d(num_features=3, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)(input_data)