input_data = torch.randn(10, 3)
output_data = torch.cummin(input_data, dim=1)