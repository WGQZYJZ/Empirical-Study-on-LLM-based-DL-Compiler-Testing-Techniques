input_data = torch.randint(20, (3, 3), dtype=torch.float)
other_data = torch.randint(10, (3, 3), dtype=torch.float)
output = torch.floor_divide(input_data, other_data)