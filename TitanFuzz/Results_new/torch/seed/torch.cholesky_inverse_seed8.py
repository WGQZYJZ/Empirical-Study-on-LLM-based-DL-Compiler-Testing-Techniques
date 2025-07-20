input = torch.randn(3, 3)
output = torch.cholesky_inverse(input)
output2 = torch.cholesky_inverse(input, upper=True)