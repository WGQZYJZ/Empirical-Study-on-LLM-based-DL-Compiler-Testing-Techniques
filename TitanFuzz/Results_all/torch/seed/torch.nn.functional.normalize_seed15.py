input_data = torch.randn(5, 3)
output_data = torch.nn.functional.normalize(input_data, dim=1)