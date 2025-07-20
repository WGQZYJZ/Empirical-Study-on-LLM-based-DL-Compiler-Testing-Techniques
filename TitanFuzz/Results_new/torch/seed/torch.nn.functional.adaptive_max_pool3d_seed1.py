input_data = torch.randn(2, 3, 5, 5, 5)
torch.nn.functional.adaptive_max_pool3d(input_data, (2, 2, 2))