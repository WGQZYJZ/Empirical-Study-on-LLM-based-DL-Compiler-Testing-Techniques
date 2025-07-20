input = torch.randint(0, 2, (4,), dtype=torch.bool)
other = torch.randint(0, 2, (4,), dtype=torch.bool)
output = torch.bitwise_and(input, other)