input_data = torch.rand(3, 4, 5)
output_data = torch.median(input_data, dim=(- 1))