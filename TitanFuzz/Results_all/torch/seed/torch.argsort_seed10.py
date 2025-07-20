input_data = torch.randn(3, 4)
output_data = torch.argsort(input_data, dim=(- 1), descending=False)