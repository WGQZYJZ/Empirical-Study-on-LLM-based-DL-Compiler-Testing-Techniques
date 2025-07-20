input_data = torch.randn(1, 1, 10)
lp_pool1d = torch.nn.functional.lp_pool1d(input_data, 1, 3, stride=3, ceil_mode=False)