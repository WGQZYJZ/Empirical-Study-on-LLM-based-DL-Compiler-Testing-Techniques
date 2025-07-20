input_data = torch.randn(5, 5)
other_data = torch.randn(5, 5)
output = torch.copysign(input_data, other_data)