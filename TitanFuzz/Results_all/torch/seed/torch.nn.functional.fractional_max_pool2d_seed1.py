input = torch.randn(1, 1, 5, 5)
output = torch.nn.functional.fractional_max_pool2d(input, kernel_size=(3, 3), output_size=(3, 3))