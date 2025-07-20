input_data = torch.randn(1, 1, 5, 5)
conv2d = torch.nn.Conv2d(1, 1, 3, 1, 1)
output = conv2d(input_data)