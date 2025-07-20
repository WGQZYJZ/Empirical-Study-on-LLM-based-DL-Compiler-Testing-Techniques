input_data = torch.randn(1, 1, 64, 64)
output_size = (4, 4)
output = torch.nn.functional.adaptive_avg_pool2d(input_data, output_size)