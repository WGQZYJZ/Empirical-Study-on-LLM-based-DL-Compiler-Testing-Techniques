input = Variable(torch.randn(20, 16, 50, 32, 32))
pool = torch.nn.FractionalMaxPool3d(kernel_size=(2, 3, 3), output_size=(10, 16, 16))
output = pool(input)