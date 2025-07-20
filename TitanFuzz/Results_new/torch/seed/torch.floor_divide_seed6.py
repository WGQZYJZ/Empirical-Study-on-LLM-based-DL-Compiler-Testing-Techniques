input_data = torch.arange(1, 10, dtype=torch.float32).reshape(3, 3)
other_data = torch.arange(1, 4, dtype=torch.float32).reshape(3, 1)
output_data = torch.floor_divide(input_data, other_data)