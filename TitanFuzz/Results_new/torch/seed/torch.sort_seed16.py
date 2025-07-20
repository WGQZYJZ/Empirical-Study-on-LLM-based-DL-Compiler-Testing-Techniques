input_data = torch.randn(1, 3, 3)
output_data = torch.sort(input_data, dim=1, descending=True)