input_data = torch.randn(1, 3, 2, 2)
output_data = torch.nn.functional.leaky_relu(input_data)