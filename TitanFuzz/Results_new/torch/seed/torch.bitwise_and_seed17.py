input = torch.randint(0, 2, (3, 3), dtype=torch.int8)
other = torch.randint(0, 2, (3, 3), dtype=torch.int8)
out = torch.bitwise_and(input, other)