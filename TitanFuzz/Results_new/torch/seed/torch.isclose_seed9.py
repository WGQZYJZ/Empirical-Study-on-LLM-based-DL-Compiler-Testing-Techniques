input = torch.randn(4, 4)
other = torch.randn(4, 4)
torch.isclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)