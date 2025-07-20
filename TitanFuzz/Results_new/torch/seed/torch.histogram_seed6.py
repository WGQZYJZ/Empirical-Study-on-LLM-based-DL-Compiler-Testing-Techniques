input_data = torch.randn(10, 3)
hist = torch.histogram(input_data, bins=10, range=((- 1), 1))
hist = torch.histogram(input_data, bins=10, range=((- 1), 1), density=True)
hist = torch.histogram(input_data, bins=10, range=((- 1), 1), density=False)