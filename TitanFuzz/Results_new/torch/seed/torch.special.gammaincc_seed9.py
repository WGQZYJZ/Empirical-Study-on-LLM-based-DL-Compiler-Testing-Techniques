input = torch.randn(2, 3, dtype=torch.float64)
other = torch.randn(2, 3, dtype=torch.float64)
output = torch.special.gammaincc(input, other)