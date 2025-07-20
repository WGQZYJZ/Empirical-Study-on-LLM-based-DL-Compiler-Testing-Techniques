input_data = torch.randn(1, 1, 5)
output_data = torch.nn.functional.lp_pool1d(input_data, 1, 3, stride=1, ceil_mode=False)
output_data = torch.nn.functional.lp_pool1d(input_data, 2, 3, stride=1, ceil_mode=False)
output_data = torch.nn.functional.lp_pool1d(input_data, float('inf'), 3, stride=1, ceil_mode=False)