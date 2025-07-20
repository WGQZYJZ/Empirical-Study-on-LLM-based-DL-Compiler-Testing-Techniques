input = torch.randn(1, 1, 3, 3)
other = torch.randn(1, 1, 3, 3)
result = torch.allclose(input, other)