input = torch.randn(1, 1, 5, 5, 5)
conv3d = torch.nn.Conv3d(1, 1, 3)
output = conv3d(input)