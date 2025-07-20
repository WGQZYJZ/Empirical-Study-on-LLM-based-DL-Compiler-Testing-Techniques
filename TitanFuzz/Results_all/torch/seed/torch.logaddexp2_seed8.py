input_data = torch.randn(2, 3, dtype=torch.float)
other_data = torch.randn(2, 3, dtype=torch.float)
output = torch.logaddexp2(input_data, other_data)