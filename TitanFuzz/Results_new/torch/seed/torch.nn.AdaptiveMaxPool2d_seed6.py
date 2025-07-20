input = torch.randn(1, 1, 9, 9)
output = torch.nn.AdaptiveMaxPool2d((3, 3))(input)