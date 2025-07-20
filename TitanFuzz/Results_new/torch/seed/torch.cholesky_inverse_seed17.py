input = torch.randn(3, 3, dtype=torch.float64)
output = torch.cholesky_inverse(input)