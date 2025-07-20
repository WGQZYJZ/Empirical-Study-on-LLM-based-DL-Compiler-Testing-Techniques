input_data = torch.randn(2, 3)
output_data = torch.nn.functional.softmin(input_data, dim=0)