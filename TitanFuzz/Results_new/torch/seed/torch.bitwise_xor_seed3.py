input_data = torch.randint(0, 2, (3, 3), dtype=torch.int64)
other_data = torch.randint(0, 2, (3, 3), dtype=torch.int64)
output = torch.bitwise_xor(input_data, other_data)