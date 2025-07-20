input_data = torch.randn(4, 4)
output_data = torch.cummin(input_data, dim=1)