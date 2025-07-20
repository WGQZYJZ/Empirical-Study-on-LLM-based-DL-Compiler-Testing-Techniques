input = torch.randn(1, 1, 6, 6, 6)
output = torch.nn.AdaptiveMaxPool3d(output_size=(3, 3, 3))(input)