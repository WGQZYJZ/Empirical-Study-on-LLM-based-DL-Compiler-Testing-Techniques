input_data = torch.randn(1, 1, 5, 5, 5)
conv3d = torch.nn.Conv3d(in_channels=1, out_channels=1, kernel_size=3)
output_data = conv3d(input_data)