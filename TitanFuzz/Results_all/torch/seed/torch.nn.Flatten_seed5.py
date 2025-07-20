data = torch.randn(2, 3, 5)
flatten = torch.nn.Flatten(start_dim=1, end_dim=(- 1))