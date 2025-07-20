input = torch.rand(4, 4)
other = torch.randint(low=1, high=10, size=(4, 4))
output = torch.ldexp(input, other)