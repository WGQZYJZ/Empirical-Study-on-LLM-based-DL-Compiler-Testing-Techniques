input = torch.randn(10, 20)
other = torch.randn(10, 20)
result = torch.allclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)