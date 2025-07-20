x = torch.randn(1, 3, 5)
batchnorm1d = torch.nn.BatchNorm1d(num_features=3, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
y = batchnorm1d(x)
x = torch.randn(1, 3, 5, 5)