data = torch.randn(1, 1, 5, 5, 5)
conv = torch.nn.Conv3d(1, 1, 3, padding=1)
out = conv(data)