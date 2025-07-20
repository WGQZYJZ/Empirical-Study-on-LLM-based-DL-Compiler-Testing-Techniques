input_data = torch.randn(1, 1, 3, 3)
output_data = torch.nn.functional.leaky_relu_(input_data, negative_slope=0.01)