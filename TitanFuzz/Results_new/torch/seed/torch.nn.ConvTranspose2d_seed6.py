input_data = torch.randn(1, 2, 10, 10)
convTranspose2d = torch.nn.ConvTranspose2d(in_channels=2, out_channels=2, kernel_size=4, stride=2, padding=1)
output = convTranspose2d(input_data)