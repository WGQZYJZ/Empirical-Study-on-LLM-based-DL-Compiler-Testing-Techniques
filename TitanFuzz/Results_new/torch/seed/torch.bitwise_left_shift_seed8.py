input = torch.randint(0, 1, (3, 3), dtype=torch.int8)
other = torch.randint(0, 1, (3, 3), dtype=torch.int8)
output = torch.bitwise_left_shift(input, other)