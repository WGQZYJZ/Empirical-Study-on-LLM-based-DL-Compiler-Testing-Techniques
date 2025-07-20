input = torch.randn(20, 16, 50, 32, 45)
output = torch.nn.AdaptiveMaxPool3d(output_size=(5, 4, 3))(input)