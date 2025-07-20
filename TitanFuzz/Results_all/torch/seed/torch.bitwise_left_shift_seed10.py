input = torch.randint(0, 2, (3, 3), dtype=torch.uint8)
other = torch.tensor([1, 2, 3], dtype=torch.uint8)
output = torch.bitwise_left_shift(input, other)