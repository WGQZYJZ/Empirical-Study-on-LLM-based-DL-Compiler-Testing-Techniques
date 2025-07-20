input_data = torch.randn(3, 4, 5)
output_data = torch.moveaxis(input_data, 0, 1)
output_data = torch.moveaxis(input_data, 0, 2)
output_data = torch.moveaxis(input_data, 1, 0)
output_data = torch.moveaxis