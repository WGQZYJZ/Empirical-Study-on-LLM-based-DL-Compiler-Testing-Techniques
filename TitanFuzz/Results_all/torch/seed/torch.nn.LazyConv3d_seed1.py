input_data = torch.randn(1, 1, 4, 4, 4)
conv3d = torch.nn.LazyConv3d(1, 1, 3)
output = conv3d(input_data)