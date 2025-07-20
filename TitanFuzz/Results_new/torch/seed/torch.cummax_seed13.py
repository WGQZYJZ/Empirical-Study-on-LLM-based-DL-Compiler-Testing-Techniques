input_data = torch.randn(3, 2)
output_data = torch.cummax(input_data, dim=1)