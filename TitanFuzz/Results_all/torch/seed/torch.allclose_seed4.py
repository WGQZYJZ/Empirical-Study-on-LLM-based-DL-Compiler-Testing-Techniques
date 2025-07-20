input = torch.randn(1, 3, 3)
other = torch.randn(1, 3, 3)
torch.allclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)