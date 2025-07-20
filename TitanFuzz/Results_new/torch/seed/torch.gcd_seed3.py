input = torch.randint(1, 10, (3, 3), dtype=torch.long)
other = torch.randint(1, 10, (3, 3), dtype=torch.long)
torch.gcd(input, other)