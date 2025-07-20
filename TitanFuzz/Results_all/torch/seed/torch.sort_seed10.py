input_data = torch.randn(1, 3, 5)
output_data = torch.sort(input_data, dim=(- 1), descending=False)