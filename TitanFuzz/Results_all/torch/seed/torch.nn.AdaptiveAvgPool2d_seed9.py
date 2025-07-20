input = torch.randn(1, 2, 5, 5)
avg_pool2d = torch.nn.AdaptiveAvgPool2d(output_size=(2, 2))
output = avg_pool2d(input)