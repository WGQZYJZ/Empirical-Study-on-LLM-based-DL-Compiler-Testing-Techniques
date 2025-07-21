input_data = torch.randn(1, 1, 1, 5)
output_data = torch.nn.functional.leaky_relu(input_data, negative_slope=0.01, inplace=False)
input_data = torch.randn(1, 1, 1, 5)