x = torch.randint(0, 2, (3, 3), dtype=torch.bool)
y = torch.randint(0, 2, (3, 3), dtype=torch.bool)
z = torch.bitwise_or(x, y)