input_data = torch.randn(20, 16, 50, 32, 32)
output = torch.nn.AdaptiveMaxPool3d(output_size=(5, 5, 5))(input_data)