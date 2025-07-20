input = torch.randint(0, 1000, (5,))
other = torch.randint(0, 1000, (5,))
output = torch.gcd(input, other)