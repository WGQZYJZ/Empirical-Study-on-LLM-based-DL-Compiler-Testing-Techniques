input_data = torch.randn(1, 1, 3, 3, 3)
output = torch.nn.ConvTranspose3d(in_channels=1, out_channels=1, kernel_size=3, stride=1, padding=0, bias=False)(input_data)