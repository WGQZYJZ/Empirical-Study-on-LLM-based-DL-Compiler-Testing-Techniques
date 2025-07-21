input_data = torch.randn(1000, 1000)
output_data = torch.nn.functional.softplus(input_data)