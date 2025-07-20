input_tensor = torch.randn(1, 1, 5)
output_tensor = torch.nn.functional.adaptive_max_pool1d(input_tensor, 3)