input_data = torch.randn(1, 10)
other_data = torch.randn(1, 10)
result = torch.special.xlogy(input_data, other_data)