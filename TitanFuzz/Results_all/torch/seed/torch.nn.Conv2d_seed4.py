input = torch.randn(1, 1, 5, 5)
conv = torch.nn.Conv2d(1, 1, 3, 1, 1)
out = conv(input)