input_data = torch.randn(1, 3)
other_data = torch.randn(1, 3)
result = torch.add(input_data, other_data)
result = torch.add(input_data, other_data, alpha=0.5)
result = torch.add(input_data, other_data, alpha=1)
result = torch.add(input_data, other_data, alpha=2)