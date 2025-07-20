input = torch.randn(1, 3, 5, 5, 5)
output_size = (3, 3, 3)
output = torch.nn.AdaptiveAvgPool3d(output_size)(input)