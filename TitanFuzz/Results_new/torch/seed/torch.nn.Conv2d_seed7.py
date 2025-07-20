input = torch.randn(1, 1, 5, 5)
conv2d = torch.nn.Conv2d(in_channels=1, out_channels=1, kernel_size=3)
output = conv2d(input)