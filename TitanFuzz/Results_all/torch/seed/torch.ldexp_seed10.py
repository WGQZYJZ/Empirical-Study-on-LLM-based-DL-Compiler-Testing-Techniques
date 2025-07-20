input = torch.randn(4)
other = torch.randint(3, (4,), dtype=torch.int32)
out = torch.ldexp(input, other)