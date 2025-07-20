input_data = torch.randn(1, 3, 5, 5)
output = torch.nn.AdaptiveAvgPool2d(output_size=(3, 3))(input_data)