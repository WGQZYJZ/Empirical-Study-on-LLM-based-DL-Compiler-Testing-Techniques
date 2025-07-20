input = torch.randn(1, 2, 3, 4, 5)
output = torch.nn.AdaptiveAvgPool3d(output_size=(1, 2, 3))(input)