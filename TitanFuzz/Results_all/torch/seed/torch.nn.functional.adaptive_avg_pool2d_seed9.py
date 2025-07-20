input_data = torch.randn(1, 1, 4, 4)
output_data = torch.nn.functional.adaptive_avg_pool2d(input_data, output_size=(1, 1))