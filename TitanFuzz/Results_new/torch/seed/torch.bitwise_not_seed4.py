input = torch.randint(0, 2, (3, 3), dtype=torch.uint8)
output = torch.bitwise_not(input)