input_data = torch.randn(2, 3)
output = torch.nn.functional.softmin(input_data, dim=1)