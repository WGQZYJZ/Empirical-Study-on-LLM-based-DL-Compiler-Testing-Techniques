input_data = torch.randn(1, 1, 5, 5)
output_data = torch.nn.LazyConvTranspose2d(1, 3, stride=2)(input_data)