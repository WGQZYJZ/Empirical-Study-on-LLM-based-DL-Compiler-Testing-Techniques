input = torch.randint(0, 2, (4, 4), dtype=torch.uint8)
output = torch.bitwise_not(input)