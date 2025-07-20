input = torch.randn(1, 16, 12, 12)
convtranspose2d = torch.nn.ConvTranspose2d(in_channels=16, out_channels=33, kernel_size=3, stride=2)
output = convtranspose2d(input)