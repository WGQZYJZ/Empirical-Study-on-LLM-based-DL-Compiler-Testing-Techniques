input = torch.randint(0, 2, (3, 3), dtype=torch.long)
other = torch.randint(0, 2, (3, 3), dtype=torch.long)
output = torch.bitwise_and(input, other)