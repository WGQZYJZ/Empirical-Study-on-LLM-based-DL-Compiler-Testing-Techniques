input = torch.randn(1, 1, 4, 4)
adaptive_avg_pool2d = torch.nn.AdaptiveAvgPool2d(output_size=2)
adaptive_avg_pool2d(input)