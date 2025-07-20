input_data = torch.randn(100)
histogram_result = torch.Tensor.histogram(input_data, bins=3, range=((- 1), 1))