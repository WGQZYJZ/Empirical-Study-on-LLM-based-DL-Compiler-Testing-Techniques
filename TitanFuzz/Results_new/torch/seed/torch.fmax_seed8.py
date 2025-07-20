input = torch.randn(1, 3)
other = torch.randn(1, 3)
result = torch.fmax(input, other)
result = torch.fmax(input, other, out=result)