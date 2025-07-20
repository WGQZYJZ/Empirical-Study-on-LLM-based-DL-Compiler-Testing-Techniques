input = torch.randn(1, 64, 8, 8, 8)
output_size = (4, 4, 4)
output = torch.nn.functional.adaptive_avg_pool3d(input, output_size)