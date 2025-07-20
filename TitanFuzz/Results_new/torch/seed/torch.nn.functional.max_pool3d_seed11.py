input_data = torch.randn(1, 1, 5, 5, 5)
output_data = torch.nn.functional.max_pool3d(input_data, kernel_size=3, stride=1, padding=1)