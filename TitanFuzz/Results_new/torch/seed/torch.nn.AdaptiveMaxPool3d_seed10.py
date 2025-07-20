input_data = torch.randn(20, 16, 50, 32, 45)
adaptive_max_pool_3d = torch.nn.AdaptiveMaxPool3d(3)
output = adaptive_max_pool_3d(input_data)