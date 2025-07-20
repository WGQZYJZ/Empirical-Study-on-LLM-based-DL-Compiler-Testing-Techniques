input_data = torch.randn(1, 2, 3, 4, 5)
conv_transpose3d = torch.nn.LazyConvTranspose3d(out_channels=3, kernel_size=3)