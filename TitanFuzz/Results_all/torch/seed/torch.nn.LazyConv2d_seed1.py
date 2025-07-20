input_data = torch.randn(1, 1, 4, 4)
conv = torch.nn.LazyConv2d(1, 3, 3, 1, 1)
output_data = conv(input_data)