input = torch.randint(10, (2, 3), dtype=torch.int16)
output = torch.randint_like(input, low=0, high=10)