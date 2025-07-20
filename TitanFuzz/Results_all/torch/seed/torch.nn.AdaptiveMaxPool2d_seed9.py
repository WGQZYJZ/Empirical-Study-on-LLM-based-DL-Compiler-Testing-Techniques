input_data = torch.randn(1, 2, 4, 4)
output = torch.nn.AdaptiveMaxPool2d((2, 2))(input_data)