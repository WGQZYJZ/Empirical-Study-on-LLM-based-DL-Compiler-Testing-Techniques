input = torch.randint(0, 10, (3, 3))
other = torch.randint(0, 10, (3, 3))
output = torch.bitwise_right_shift(input, other)