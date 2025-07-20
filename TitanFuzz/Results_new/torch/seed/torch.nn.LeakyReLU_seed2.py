input_data = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
leaky_relu = torch.nn.LeakyReLU(negative_slope=0.01, inplace=False)
output_data = leaky_relu(input_data)