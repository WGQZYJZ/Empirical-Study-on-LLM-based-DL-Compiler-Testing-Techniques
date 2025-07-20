input_data = torch.rand(1, 1, 5)
output_data = torch.nn.functional.lp_pool1d(input_data, norm_type=2, kernel_size=3, stride=2, ceil_mode=False)