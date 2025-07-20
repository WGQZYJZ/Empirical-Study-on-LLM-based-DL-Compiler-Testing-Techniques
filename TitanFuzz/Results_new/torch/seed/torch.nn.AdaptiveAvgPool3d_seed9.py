input = torch.randn(1, 1, 4, 4, 4)
output = torch.nn.AdaptiveAvgPool3d(output_size=1)(input)