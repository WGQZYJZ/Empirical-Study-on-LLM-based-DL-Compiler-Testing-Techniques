input = torch.randn(3, 3)
other = torch.randn(3, 3)
result = torch.gt(input, other)
result = torch.gt(input, other, out=torch.empty_like(input))