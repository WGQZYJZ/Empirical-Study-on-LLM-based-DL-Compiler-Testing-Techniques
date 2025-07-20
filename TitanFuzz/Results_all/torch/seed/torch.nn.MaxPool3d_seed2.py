in_channels = 1
input_size = (1, in_channels, 4, 4, 4)
input = Variable(torch.randn(input_size))
pool = torch.nn.MaxPool3d(kernel_size=2)
output = pool(input)