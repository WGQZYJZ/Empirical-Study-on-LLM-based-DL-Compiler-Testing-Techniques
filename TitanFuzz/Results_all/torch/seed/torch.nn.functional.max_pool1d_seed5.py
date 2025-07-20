input_data = torch.randn(1, 1, 3)
max_pool_output = torch.nn.functional.max_pool1d(input_data, 2)