input = torch.randn(1, 1, 5, 5)
output = torch.nn.functional.adaptive_avg_pool2d(input, (2, 2))