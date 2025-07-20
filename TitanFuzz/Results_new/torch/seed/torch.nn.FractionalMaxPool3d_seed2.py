input = Variable(torch.randn(20, 16, 50, 32, 45))
output = torch.nn.FractionalMaxPool3d(kernel_size=(3, 2, 2), output_size=(5, 16, 22))(input)
output = torch.nn.FractionalMaxPool3d