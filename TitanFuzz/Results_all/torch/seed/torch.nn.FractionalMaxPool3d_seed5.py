input = torch.randn(20, 16, 50, 32, 45)
output = torch.nn.FractionalMaxPool3d(kernel_size=(3, 5, 3), output_size=(5, 10, 3))(input)