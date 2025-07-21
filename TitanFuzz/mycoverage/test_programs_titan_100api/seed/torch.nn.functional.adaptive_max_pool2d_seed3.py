input = torch.randn(1, 1, 5, 5)
output = torch.nn.functional.adaptive_max_pool2d(input, (1, 1))