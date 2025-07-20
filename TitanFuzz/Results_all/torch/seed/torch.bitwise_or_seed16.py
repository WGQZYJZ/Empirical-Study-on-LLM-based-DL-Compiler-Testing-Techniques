input = torch.randint(0, 2, (2, 3), dtype=torch.bool)
other = torch.randint(0, 2, (2, 3), dtype=torch.bool)
out = torch.bitwise_or(input, other)