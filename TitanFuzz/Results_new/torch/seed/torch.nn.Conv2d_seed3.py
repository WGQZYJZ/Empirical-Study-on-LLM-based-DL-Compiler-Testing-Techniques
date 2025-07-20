input = Variable(torch.randn(1, 3, 5, 5))
conv_layer = torch.nn.Conv2d(in_channels=3, out_channels=1, kernel_size=3, stride=1, padding=1)
output = conv_layer(input)