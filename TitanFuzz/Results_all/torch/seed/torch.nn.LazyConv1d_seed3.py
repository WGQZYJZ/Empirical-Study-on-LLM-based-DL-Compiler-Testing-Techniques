x = torch.randn(2, 3, 10)
conv1d = torch.nn.LazyConv1d(out_channels=2, kernel_size=3, stride=2)
y = conv1d(x)