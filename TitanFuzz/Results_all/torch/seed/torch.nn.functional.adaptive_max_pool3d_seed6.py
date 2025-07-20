input_data = torch.randn(1, 1, 32, 32, 32)
output_data = torch.nn.functional.adaptive_max_pool3d(input_data, (1, 1, 1))