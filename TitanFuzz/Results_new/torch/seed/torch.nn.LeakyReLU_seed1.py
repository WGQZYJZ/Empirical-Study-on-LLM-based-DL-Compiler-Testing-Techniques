input_data = torch.tensor([(- 1), 0, 1], dtype=torch.float)
relu_layer = torch.nn.LeakyReLU(negative_slope=0.01, inplace=False)
output_data = relu_layer(input_data)