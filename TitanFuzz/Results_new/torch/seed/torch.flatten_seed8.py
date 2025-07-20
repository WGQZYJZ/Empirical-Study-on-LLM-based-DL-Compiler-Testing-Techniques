input_data = torch.randn(1, 3, 5, 5)
output_data = torch.flatten(input_data, start_dim=1)