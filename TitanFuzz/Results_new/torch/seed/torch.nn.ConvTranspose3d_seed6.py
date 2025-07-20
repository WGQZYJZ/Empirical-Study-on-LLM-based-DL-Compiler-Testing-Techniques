input_data = torch.rand(1, 1, 5, 5, 5)
conv_transpose3d = torch.nn.ConvTranspose3d(in_channels=1, out_channels=1, kernel_size=(3, 3, 3))
output = conv_transpose3d(input_data)