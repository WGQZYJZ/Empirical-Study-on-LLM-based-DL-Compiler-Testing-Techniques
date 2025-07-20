input_data = torch.randn(1, 1, 10)
output_data = torch.nn.functional.adaptive_avg_pool1d(input_data, output_size=5)
input_data = torch.randn(1, 1, 10, 10)