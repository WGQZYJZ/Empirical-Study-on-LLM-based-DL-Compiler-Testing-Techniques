input_data = torch.randn(3, 3)
leaky_relu = torch.nn.LeakyReLU(negative_slope=0.01, inplace=False)
output = leaky_relu(input_data)