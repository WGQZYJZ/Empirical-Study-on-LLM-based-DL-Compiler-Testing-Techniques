input_data = torch.randn(4, 4)
other_data = torch.randn(4, 4)
output = torch.logaddexp2(input_data, other_data)