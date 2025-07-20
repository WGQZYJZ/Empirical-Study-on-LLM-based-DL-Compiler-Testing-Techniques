input_data = torch.randn(1, 3, 8, 8, 8)
output = torch.nn.functional.fractional_max_pool3d(input_data, kernel_size=(3, 3, 3), output_size=(3, 3, 3))