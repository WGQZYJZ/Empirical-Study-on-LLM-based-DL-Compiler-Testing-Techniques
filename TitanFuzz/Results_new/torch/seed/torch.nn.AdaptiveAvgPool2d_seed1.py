input = torch.randn(1, 1, 4, 4)
avg_pool2d = torch.nn.AdaptiveAvgPool2d(output_size=(2, 2))
output = avg_pool2d(input)