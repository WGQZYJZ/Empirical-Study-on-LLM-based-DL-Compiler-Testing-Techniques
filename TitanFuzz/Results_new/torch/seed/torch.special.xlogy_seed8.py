input = torch.randn(4, 4)
other = torch.randn(4, 4)
out = torch.special.xlogy(input, other)
out = torch.special.xlogy(input, other, out=torch.empty(4, 4))