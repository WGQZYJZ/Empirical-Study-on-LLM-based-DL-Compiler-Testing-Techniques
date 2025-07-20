input_data = torch.randn(2, 3)
leaky_relu = torch.nn.LeakyReLU(negative_slope=0.01, inplace=False)
output_data = leaky_relu(input_data)