input_data = torch.randn(1, 3)
output_data = torch.argsort(input_data, dim=(- 1), descending=False)