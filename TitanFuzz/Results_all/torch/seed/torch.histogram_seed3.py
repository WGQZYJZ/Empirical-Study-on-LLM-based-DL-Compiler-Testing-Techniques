input = torch.randn(100000, dtype=torch.float32)
hist = torch.histogram(input, bins=10, range=((- 3), 3))
hist = torch.histogram(input, bins=10, range=((- 3), 3), density=True)