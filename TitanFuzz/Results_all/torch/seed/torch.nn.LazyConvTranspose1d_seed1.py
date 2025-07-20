input_data = torch.randn(3, 5, 7)
conv1d_transpose = torch.nn.LazyConvTranspose1d(3, 2, stride=2, padding=1)
output_data = conv1d_transpose(input_data)