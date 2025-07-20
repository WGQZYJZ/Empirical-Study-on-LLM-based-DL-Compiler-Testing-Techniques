input = torch.randn(1, 1, 7, 7)
output = torch.nn.FractionalMaxPool2d(3, output_size=(3, 3))(input)