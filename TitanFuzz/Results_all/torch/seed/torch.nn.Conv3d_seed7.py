input_data = Variable(torch.randn(1, 1, 3, 3, 3))
conv3d_layer = torch.nn.Conv3d(in_channels=1, out_channels=1, kernel_size=3, stride=1, padding=0)
output = conv3d_layer(input_data)