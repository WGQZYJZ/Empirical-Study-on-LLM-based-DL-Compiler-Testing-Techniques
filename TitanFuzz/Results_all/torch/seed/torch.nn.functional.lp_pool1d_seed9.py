input_data = torch.randn(1, 1, 4)
output_data = torch.nn.functional.lp_pool1d(input_data, 1, 2, stride=2)