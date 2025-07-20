input = torch.randn(3, 4, dtype=torch.float)
other = torch.randn(3, 4, dtype=torch.float)
output = torch.special.gammainc(input, other)