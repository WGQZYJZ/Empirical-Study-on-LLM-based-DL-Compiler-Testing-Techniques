x = torch.randn(3, 5)
relu = torch.nn.LeakyReLU(negative_slope=0.01, inplace=False)