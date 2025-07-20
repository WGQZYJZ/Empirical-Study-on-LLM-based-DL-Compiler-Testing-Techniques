input_data = torch.randn(2, 3, 5)
output_data = torch.permute(input_data, (2, 0, 1))