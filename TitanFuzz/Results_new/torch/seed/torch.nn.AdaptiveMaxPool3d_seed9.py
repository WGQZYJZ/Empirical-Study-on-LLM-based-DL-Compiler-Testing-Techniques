input_data = torch.randn(1, 2, 3, 4, 5)
output = torch.nn.AdaptiveMaxPool3d(output_size=(1, 2, 3))(input_data)