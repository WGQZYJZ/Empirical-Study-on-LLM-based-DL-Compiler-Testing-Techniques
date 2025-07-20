input_data = torch.randn(1, 1, 10)
conv1d = torch.nn.LazyConv1d(1, 3, stride=1, padding=1)
output = conv1d(input_data)