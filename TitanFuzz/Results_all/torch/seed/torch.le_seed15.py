input = torch.randn(2, 2)
other = torch.randn(2, 2)
output = torch.le(input, other)
output = torch.le(input, other, out=None)