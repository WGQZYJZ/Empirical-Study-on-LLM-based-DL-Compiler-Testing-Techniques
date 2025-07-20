x = torch.randn(100, 10)
bn = torch.nn.BatchNorm1d(num_features=10)
y = bn(x)