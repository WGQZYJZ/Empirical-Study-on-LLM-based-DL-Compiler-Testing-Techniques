input_data = torch.randn(1, 1, 8)
output = torch.nn.functional.adaptive_max_pool1d(input_data, 3)