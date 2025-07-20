input_data = torch.randint(low=0, high=2, size=(3, 3), dtype=torch.int32)
other_data = torch.randint(low=0, high=2, size=(3, 3), dtype=torch.int32)
result = torch.bitwise_or(input_data, other_data)