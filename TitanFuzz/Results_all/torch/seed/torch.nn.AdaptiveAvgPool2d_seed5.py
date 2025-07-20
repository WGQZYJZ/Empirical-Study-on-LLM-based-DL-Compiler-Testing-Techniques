input = torch.randn(1, 3, 5, 5)
output = torch.nn.AdaptiveAvgPool2d(3)(input)