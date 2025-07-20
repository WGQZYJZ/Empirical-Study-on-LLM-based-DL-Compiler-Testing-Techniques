input = torch.randint(0, 2, (3, 3), dtype=torch.int)
other = torch.randint(0, 2, (3, 3), dtype=torch.int)
out = torch.bitwise_or(input, other)