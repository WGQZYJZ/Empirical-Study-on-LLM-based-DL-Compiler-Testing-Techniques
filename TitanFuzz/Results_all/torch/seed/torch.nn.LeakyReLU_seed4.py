input_data = torch.tensor([(- 1), (- 0.5), 0, 0.5, 1], dtype=torch.float)
leaky_relu = torch.nn.LeakyReLU(negative_slope=0.01, inplace=False)
output_data = leaky_relu(input_data)