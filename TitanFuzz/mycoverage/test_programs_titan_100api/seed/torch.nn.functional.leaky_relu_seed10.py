input_data = torch.tensor([(- 1), 0, 1, 2, 3], dtype=torch.float32)
output_data = torch.nn.functional.leaky_relu(input_data, negative_slope=0.01, inplace=False)