input_data = torch.rand(1, 3, 10)
output_data = torch.nn.functional.lp_pool1d(input_data, 1, 3, 1)