input = torch.randn(1, 3, 5, 7, 9)
output = torch.nn.AdaptiveAvgPool3d(3)(input)