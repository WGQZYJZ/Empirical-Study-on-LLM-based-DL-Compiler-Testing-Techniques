input = torch.randn(3, 4)
other = torch.randn(3, 4)
torch.allclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)