input = torch.randn(1, 1, 4, 4)
output = torch.nn.AdaptiveMaxPool2d(output_size=(2, 2))(input)