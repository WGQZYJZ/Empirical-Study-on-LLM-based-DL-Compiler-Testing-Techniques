x = torch.rand(5, 3)
y = torch.rand(5, 3)
torch.allclose(x, y, rtol=1e-05, atol=1e-08, equal_nan=False)