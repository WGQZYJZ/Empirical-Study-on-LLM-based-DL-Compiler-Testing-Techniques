input = torch.randn(1, 1, 5, 5, 5)
output_size = (3, 3, 3)
output = torch.nn.functional.adaptive_max_pool3d(input, output_size)