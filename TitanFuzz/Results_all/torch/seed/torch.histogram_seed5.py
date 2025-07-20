input = torch.rand(1000)
histogram = torch.histogram(input, bins=10, range=(0, 1))