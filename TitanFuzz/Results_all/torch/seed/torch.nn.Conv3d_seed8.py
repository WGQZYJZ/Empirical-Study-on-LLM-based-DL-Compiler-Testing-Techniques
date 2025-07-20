input = torch.randn(1, 1, 5, 5, 5)
conv3d = torch.nn.Conv3d(1, 1, 2, stride=1, padding=0)