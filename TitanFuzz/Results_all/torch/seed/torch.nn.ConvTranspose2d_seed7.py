input_data = torch.rand(1, 1, 5, 5)
conv_transpose = torch.nn.ConvTranspose2d(in_channels=1, out_channels=1, kernel_size=3, stride=2, padding=1)
output_data = conv_transpose(input_data)