input = torch.randint(0, 10, (4, 4), dtype=torch.int32)
output = torch.bitwise_left_shift(input, 2)